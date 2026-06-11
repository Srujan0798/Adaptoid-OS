# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 4.0.x | ✅ |
| 3.x | ⚠️ Critical fixes only |
| < 3.0 | ❌ |

## Reporting a Vulnerability

Email: security@adaptoid-os.dev (placeholder — update when real)

Please include:
1. FM number (if matches a known failure mode)
2. Steps to reproduce
3. Impact assessment
4. Suggested fix (optional)

## Response Timeline

| Severity | Acknowledgment | Fix Target |
|---|---|---|
| Critical | 24 hours | 72 hours |
| High | 48 hours | 1 week |
| Medium | 1 week | 1 month |
| Low | 1 month | Next minor release |

## Security-Related Validators

- `validators/oap_security.sh` — policy enforcement
- `validators/vault_mmu.sh` — state integrity
- `validators/publish_gate.sh` — prevents secret leakage

## OAP Default Policy

By default, all tool calls require explicit policy. No policy = DENY.
See `templates/root/policies/default.yaml`.
