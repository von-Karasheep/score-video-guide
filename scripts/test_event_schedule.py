"""Small regressions for real failure modes; no media or external dependencies."""
import copy
import unittest
from check_event_schedule import audit


class EventScheduleTests(unittest.TestCase):
    def fixture(self):
        event = {"event_id": "note-o1", "occurrence_id": "m1-o1", "kind": "attack",
                 "sample": 48000, "expected_pitches": [60, 72],
                 "detected_pitches": [60, 72], "evidence": "review/clip.mp4"}
        windows = [{"occurrence_id": "m1-o1", "start_frame": 0, "end_frame": 90},
                   {"occurrence_id": "m2-o1", "start_frame": 90, "end_frame": 180}]
        return event, windows

    def test_correct_candidate_never_becomes_music_approval(self):
        event, windows = self.fixture()
        result = audit([event], windows, sample_rate=48000)
        self.assertTrue(result["structural_pass"])
        self.assertTrue(result["coverage_complete"])
        self.assertFalse(result["music_verified"])

    def test_premature_measure_switch_is_caught(self):
        event, windows = self.fixture()
        windows[0]["end_frame"] = 30
        windows[1]["start_frame"] = 30
        self.assertEqual(len(audit([event], windows, sample_rate=48000)["frame_label_mismatches"]), 1)

    def test_continuation_does_not_inflate_attack_coverage(self):
        event, windows = self.fixture()
        event.update(kind="continuation", sample=None)
        result = audit([event], windows, sample_rate=48000)
        self.assertEqual(result["expected_attack_groups"], 0)
        self.assertEqual(result["continuation_groups"], 1)
        event.update(sample=48000, anchor_method="physical_onset")
        self.assertFalse(audit([event], windows, sample_rate=48000)["structural_pass"])

    def test_octave_error_is_not_hidden_by_pitch_class(self):
        event, windows = self.fixture()
        event["detected_pitches"] = [60]
        result = audit([event], windows, sample_rate=48000)
        self.assertEqual(result["undercovered_pitch_groups"][0]["missing_pitches"], [72])

    def test_unknown_and_imprecise_candidates_remain_visible(self):
        event, windows = self.fixture()
        event["onset_interval_samples"] = [47000, 50000]
        missing = dict(event, event_id="missing", sample=None)
        result = audit([event, missing], windows, sample_rate=48000)
        self.assertFalse(result["coverage_complete"])
        self.assertEqual(result["unmatched_attack_ids"], ["missing"])
        self.assertEqual(result["wide_uncertainty_ids"], ["note-o1"])

    def test_repeated_source_note_keeps_distinct_occurrences(self):
        event, windows = self.fixture()
        event["source_id"] = "printed-note"
        second = dict(event, event_id="note-o2", occurrence_id="m2-o1", sample=160000)
        result = audit([event, second], windows, sample_rate=48000)
        self.assertEqual(result["expected_attack_groups"], 2)
        self.assertTrue(result["structural_pass"])

    def test_rational_frame_rate_uses_integer_sample_clock(self):
        event, windows = self.fixture()
        event["sample"] = 48048
        result = audit([event], windows, sample_rate=48000, fps="30000/1001", intro_samples=96096)
        self.assertEqual(result["frame_label_mismatches"][0]["frame"], 90)

    def test_invalid_or_duplicate_ids_and_intervals_fail(self):
        event, windows = self.fixture()
        with self.assertRaises(ValueError):
            audit([event, copy.deepcopy(event)], windows, sample_rate=48000)
        event["onset_interval_samples"] = [49000, 50000]
        with self.assertRaises(ValueError):
            audit([event], windows, sample_rate=48000)
        event["sample"] = 1.0
        with self.assertRaises(ValueError):
            audit([event], windows, sample_rate=48000)


if __name__ == "__main__":
    unittest.main()
