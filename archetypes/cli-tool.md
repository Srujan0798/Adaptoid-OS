# Archetype — CLI Tool / Library / Package

**Signals.** "CLI", "library", "package", "npm/pip publish", "SDK", "command-line", reusable by other developers.

**Default tier.** T1, with packaging polish.

## Emphasize
- **API/CLI design first.** The interface is the product. Design the commands/functions before implementing.
- **Great docs + examples.** README with copy-pasteable examples; every public function documented.
- **Semantic versioning + changelog.** Consumers depend on stability.
- **Cross-platform / cross-version tests.** Matrix CI (Python 3.10/11/12 or Node 18/20/22).
- **Zero/minimal dependencies.** Every dep is a liability for consumers.
- **Helpful errors.** A library's error messages are its UX.

## Skip
- UI, multi-tenancy, deployment infra, observability stack
- Heavy `docs/operational`
- `deliverables/`

## Folders
- `src/<package>/`, `tests/` (unit + matrix), `examples/`, `docs/` (API ref, usage), `README.md`, `CHANGELOG.md`, packaging config (`pyproject.toml`/`package.json`), CI matrix.
- Omit: `.specify/` heavy, `orchestrator/` can be lean, `docs/operational`, `docs/compliance`.

## Highest-risk failure modes
- **FM-03 broken references** — examples/docs referencing removed APIs = broken docs.
- **FM-05 / FM-12** — version numbers + examples in README must match the actual released API.
- **FM-10 flaky tests** — published library with flaky CI erodes trust fast.
- **FM-08 scope creep** — a library that does too much is a library nobody adopts.

## Definition of done
- Public API stable + documented + exemplified
- Matrix CI green across supported versions
- `pip install`/`npm install` then the README example works verbatim
- CHANGELOG + semver tag

## Deliverables
- The package (published or publishable)
- README with working examples
- API reference + CHANGELOG
