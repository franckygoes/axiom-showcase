# Emblematic scenario matrix

The private AXIOM release executes four closed, local demonstration domains.
Every domain is exercised through the same four governed outcomes.

| Domain | Data boundary | Nominal | Ambiguous | Contradiction | Tamper |
| --- | --- | --- | --- | --- | --- |
| Cybersecurity | Fully synthetic defensive dossier | `ALLOW` | `NEEDS_INPUT` | `REVIEW` | `BLOCK` |
| OSINT | Frozen, authorized and fictional corpus | `ALLOW` | `NEEDS_INPUT` | `REVIEW` | `BLOCK` |
| Market analysis | Synthetic historical observations; no advice or order | `ALLOW` | `NEEDS_INPUT` | `REVIEW` | `BLOCK` |
| Fraud triage | Fully synthetic evidence; no accusation or account action | `ALLOW` | `NEEDS_INPUT` | `REVIEW` | `BLOCK` |

## Interpretation

- `ALLOW` means the local result satisfied the exact registered contract.
- `NEEDS_INPUT` stops before governed agent execution.
- `REVIEW` preserves a contradiction for a human decision.
- `BLOCK` stops altered evidence before the first Ruche message.

The 16 scenario outcomes do not claim coverage of every real-world situation.
They prove the declared closed contracts and their negative paths.
