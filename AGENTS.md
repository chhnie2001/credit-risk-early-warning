# Repository Working Agreement

These instructions apply to all work in this repository.

## Development standards

- Keep changes small, modular, and easy for a beginner to review.
- Prefer focused files and functions with a single clear responsibility.
- Add type hints and useful docstrings to Python functions, classes, and modules.
- Explain the purpose, approach, assumptions, and trade-offs before making major changes.
- Do not fabricate data sources, analytical findings, model performance, credit opinions, or business impact.
- Do not hard-code outputs to reproduce a desired conclusion or resume claim.

## Data and analytical controls

- Use only synthetic data or properly documented public data.
- Never add confidential, proprietary, personally identifiable, or material non-public information.
- Clearly label synthetic data and distinguish demonstrations from empirical findings.
- Reconcile data between source, intermediate, and final layers; document expected row counts, totals, keys, and exceptions where relevant.
- Treat missing, stale, duplicated, or inconsistent data explicitly rather than silently discarding it.

## Testing and review

- Add tests for important business rules, including score boundaries, warning thresholds, data-quality checks, and reconciliation logic.
- Run relevant checks after every change and report the results honestly.
- Do not weaken tests merely to make a failing change pass.
- Keep documentation synchronized with implemented behavior.

## Change management

- Make Git checkpoints after stable, verified milestones.
- Use concise commit messages that describe the completed milestone.
- Do not combine unrelated changes in one checkpoint.
- Do not install or add a package without first explaining its purpose and why the existing stack is insufficient.
