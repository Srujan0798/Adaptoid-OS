# Calibration

## Purpose

Calibrate **harness behavior** (not model IQ):

- archetype + tier detection
- host emission
- scope box (FM-08)
- evidence-or-it-didn't-happen (FM-09)
- handoff / wake (FM-14)

## Files

| File | Role |
|---|---|
| `code.yaml` | Original code-generation sketch |
| `generate_cases.py` | Builds 50 harness cases |
| `cases.json` | Generated 50-case set |
| `run_calibration_smoke.sh` | Runs a sample of cases through the engine |

## Generate / run

```bash
python3 calibration/generate_cases.py
bash calibration/run_calibration_smoke.sh
```

Full 50-case model eval loops are intentional opt-in (costly). Smoke covers structure + engine emit for a sample.
