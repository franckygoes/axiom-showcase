# AXIOM — Public Evidence Showcase

AXIOM is a local-first, fail-closed architecture for planning, executing and
reviewing bounded AI-agent missions. It separates mission framing, agent
execution, independent validation, governance decisions and human approval.

This repository is a **documentation and evidence showcase**. It demonstrates
the verified behavior and boundaries of the private AXIOM implementation
without distributing its proprietary runtime, policies, private plugins or
development history.

## What AXIOM proves today

- missions are accepted only through explicit contracts and closed profiles;
- ambiguous inputs stop with `NEEDS_INPUT` before agent execution;
- governed agents communicate through registered, auditable routes;
- independent governance produces `ALLOW`, `REVIEW` or `BLOCK`;
- altered evidence is blocked before the first agent message;
- authenticated journals support controlled interruption and exact recovery;
- completed stages are not silently replayed;
- Mission Control remains local and requires explicit human gates.

## Verified private release

| Item | Verified value |
| --- | --- |
| AXIOM Suite | `v1.2.0` |
| AXIOM Platform | `v1.1.0` |
| Platform tests | `406` |
| Governance Skills | `5` |
| Plugin package | `PASS` |
| GPT-to-Skills migrations | `5` |
| Emblematic profiles | `4` |
| Emblematic scenarios | `16` |
| Persistence and recovery scenarios | `10` |
| Bounded claim/evidence entries | `20` |

Latest local verification, performed on 8 November 2026:

```text
AXIOM_SUITE_CHECK=PASS suite_version=1.2.0 platform_version=1.1.0 manifest_files=32 platform_tests=406 skills=5 plugin=PASS migrations=5
```

The structured record is available in
[`evidence/verification-summary.json`](evidence/verification-summary.json).

## Architecture

```text
Mission Contract + Case File
            |
            v
      AXIOM ELITE
  omissions / contradictions / risk
            |
            v
   Prompty Planner + Prompt Kernel
            |
            v
       Verified Hive Plan
            |
            v
  Ruche: governed specialist agents
            |
            v
 Governance Kernel: ALLOW / REVIEW / BLOCK
            |
            v
 Authenticated Run Journal + Mission Control
            |
            v
      Explicit human decision
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the component map and
[`evidence/SCENARIO_MATRIX.md`](evidence/SCENARIO_MATRIX.md) for the four
demonstration domains.

## Safety boundary

The demonstrations use synthetic, historical or frozen authorized data. They
do not perform live trading, active OSINT collection, account enforcement,
publication, purchases or any external side effect.

This showcase does not claim that AXIOM is a universal safety system or a
production identity platform. It demonstrates a bounded and testable governance
architecture.

## Public status

No public license has been selected for AXIOM. The absence of a `LICENSE` file
means that no permission to copy, modify, redistribute or reuse the contents is
granted. All rights are reserved by Franck Melka / TechToolGeek.

The private engineering repository and `axiom-meta-hackathon` are not mirrored,
modified or exposed here.
