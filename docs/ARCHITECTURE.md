# AXIOM architecture — public map

## Governed execution chain

```mermaid
flowchart TD
    A[Mission Contract and Case File] --> B[AXIOM ELITE]
    B -->|NEEDS_INPUT| H[Human clarification]
    B -->|PASS| C[Prompty Planner and Prompt Kernel]
    C --> D[Verified Hive Plan]
    D --> E[Ruche]
    E --> E1[Sentinel]
    E1 --> E2[Analyst]
    E2 --> E3[Contradictor]
    E3 --> E4[Briefing]
    E4 --> F[Governance Kernel]
    F -->|ALLOW| G[Bounded candidate result]
    F -->|REVIEW| I[Human review required]
    F -->|BLOCK| J[Fail-closed stop]
    D --> K[Authenticated Run Journal]
    E --> K
    F --> K
    K --> L[Local Mission Control]
```

## Responsibility boundaries

| Component | Responsibility | Explicit limit |
| --- | --- | --- |
| Mission Contract | Declares objective, inputs, constraints and permitted actions | Does not grant general autonomy |
| AXIOM ELITE | Detects omissions, contradictions, assumptions and under-declared risk | Does not approve the mission |
| Prompty Planner | Produces a bounded plan from approved profiles | Cannot freely invent agents or routes |
| Ruche | Executes registered specialist roles through direct governed messages | No uncontrolled intermediary and no external authority |
| Governance Kernel | Applies versioned policy and returns `ALLOW`, `REVIEW` or `BLOCK` | An `ALLOW` remains local to the declared contract |
| Run Journal | Authenticates stages, artifacts and recovery bindings | Is not an identity or non-repudiation service |
| Mission Control | Shows evidence and enforces explicit human gates | Loopback-only, single local operator |

## Fail-closed invariants

AXIOM stops when it encounters an unknown contract, altered evidence, an
unregistered route, a missing approval, a version mismatch, an invalid recovery
binding or an unauthorized action class.

Technical completion and governance approval are separate states. A completed
agent run can still end in `REVIEW` or `BLOCK`.
