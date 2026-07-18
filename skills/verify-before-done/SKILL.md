---
name: verify-before-done
description: >
  Use before claiming done, ship, or PR. Run acceptance commands and preflight; paste exit codes.
---

# Verify before done

1. Run the task `acceptance` command(s); require exit 0.
2. Run `bash orchestrator/scripts/preflight.sh .`
3. Paste command + output in the report. No green claim without evidence.
4. If background tasks were started, wait for exit codes first.

Status without evidence = false (FM-09).
