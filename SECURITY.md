# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 5.1.x | ✅ |
| 5.0.x | ✅ security fixes |
| 4.0.x | ⚠️ critical only |
| < 4.0 | ❌ |

## Reporting a Vulnerability

Open a private report via GitHub Security Advisories:  
https://github.com/Srujan0798/Adaptoid-OS/security/advisories/new

Include:
1. FM number if it matches a known failure mode
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
- `validators/publish_gate.sh` — secret / embarrassment gate
- `validators/route_sentinel.sh` — wrong-route blocking

## OAP Default Policy

By default, destructive and network tool patterns ask or deny. See `templates/root/policies/default.yaml`.

## Scope note

Adaptoid is a **harness kit** (markdown + shell + small Python). Treat generated project policies as starting points; harden for your production blast radius.
