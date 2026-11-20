"""Audit candidate attack groups against an exact output-frame schedule.

This checks data consistency, never listening accuracy. Samples are relative
to prepared music PCM; presentation-only silence is intro_samples.
"""
from bisect import bisect_right
from fractions import Fraction


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def audit(events, schedule, *, sample_rate, fps=30, intro_samples=0):
    rate = _integer(sample_rate, "sample_rate", 1)
    intro = _integer(intro_samples, "intro_samples")
    if not isinstance(fps, (int, str, Fraction)) or isinstance(fps, bool):
        raise ValueError("fps must be an integer or rational string")
    frame_rate = Fraction(fps)
    if frame_rate <= 0:
        raise ValueError("fps must be positive")
    windows = sorted(schedule, key=lambda row: row["start_frame"])
    errors, mismatches, missing, undercovered = [], [], [], []
    unchecked, wide, evidence_missing = [], [], []
    previous_end = None
    for row in windows:
        start = _integer(row["start_frame"], "start_frame")
        end = _integer(row["end_frame"], "end_frame")
        if not row.get("occurrence_id") or end <= start:
            raise ValueError("schedule requires occurrence_id and a positive frame interval")
        if previous_end is not None and start < previous_end:
            errors.append("overlapping frame windows")
        previous_end = end
    starts = [row["start_frame"] for row in windows]
    ids, attacks, matched, continuations = set(), 0, 0, 0
    previous_attack = None
    kinds = {"attack", "grace", "continuation", "rest", "cue"}
    for event in events:
        identity = event["event_id"]
        if not identity or identity in ids:
            raise ValueError("event_id must be nonempty and unique across occurrences")
        ids.add(identity)
        kind = event["kind"]
        if kind not in kinds or not event.get("occurrence_id"):
            raise ValueError("invalid kind or missing occurrence_id")
        is_attack = kind in {"attack", "grace"}
        attacks += is_attack
        continuations += kind == "continuation"
        if not is_attack and event.get("anchor_method") == "physical_onset":
            errors.append(f"{identity}: continuation/rest/cue is not a new attack")
        sample = event.get("sample")
        if sample is None:
            if is_attack:
                missing.append(identity)
            continue
        sample = _integer(sample, "sample")
        if is_attack:
            matched += 1
            if previous_attack is not None and sample <= previous_attack:
                errors.append(f"{identity}: attacks must increase; group simultaneous pitches together")
            previous_attack = sample
            if not event.get("evidence"):
                evidence_missing.append(identity)
            expected = event.get("expected_pitches")
            detected = event.get("detected_pitches")
            if expected is None or detected is None:
                unchecked.append(identity)
            else:
                for pitch in list(expected) + list(detected):
                    _integer(pitch, "MIDI pitch")
                    if pitch > 127:
                        raise ValueError("nonstandard pitch requires an explicit adapter")
                absent = sorted(set(expected) - set(detected))
                if absent:
                    undercovered.append({"event_id": identity, "missing_pitches": absent})
        interval = event.get("onset_interval_samples")
        if interval is not None:
            lo, hi = interval
            lo = _integer(lo, "onset lower bound")
            hi = _integer(hi, "onset upper bound")
            if not lo <= sample <= hi:
                raise ValueError("sample must lie inside onset_interval_samples")
            if (hi - lo) * frame_rate.numerator > rate * frame_rate.denominator:
                wide.append(identity)
        numerator = (sample + intro) * frame_rate.numerator
        denominator = rate * frame_rate.denominator
        frame = (numerator + denominator - 1) // denominator
        index = bisect_right(starts, frame) - 1
        visible = windows[index] if index >= 0 and frame < windows[index]["end_frame"] else None
        wrong = visible is None or visible["occurrence_id"] != event["occurrence_id"]
        if visible is not None and event.get("system_id") is not None:
            wrong = wrong or visible.get("system_id") != event["system_id"]
        if wrong:
            mismatches.append({"event_id": identity, "frame": frame,
                               "expected_occurrence": event["occurrence_id"],
                               "visible_occurrence": visible["occurrence_id"] if visible else None})
    return {"structural_pass": not errors and not mismatches,
            "expected_attack_groups": attacks, "matched_attack_groups": matched,
            "continuation_groups": continuations, "coverage_complete": not missing,
            "unmatched_attack_ids": missing, "undercovered_pitch_groups": undercovered,
            "pitch_unchecked_ids": unchecked, "wide_uncertainty_ids": wide,
            "evidence_missing_ids": evidence_missing, "frame_label_mismatches": mismatches,
            "errors": errors, "music_verified": False,
            "scope": "candidate_data_consistency_only"}
