# Attic v5.1.2 — orphan / disconnected cut

Files removed from the **live product spine** because they were:

- leftover from another timeline (super-adaptoid validators without protocols)
- optional adapters not used by Core engine (claw_bridge, skills)
- parallel workflow YAMLs unused by `init-wave --sdlc`
- long-form adaptor prose not executed by `engine.py`
- protocols not referenced by kernel/SDLC/preflight

## Live spine only

See repo root `FLOW.md`.

## Restore

```bash
cp -R docs/historical/attic-v5.1.2-orphans/<path> ./
```
