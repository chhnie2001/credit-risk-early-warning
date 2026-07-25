# Project Scope

## Business problem

Issuer credit monitoring often requires analysts to combine financial statements, market signals, and qualitative observations across many issuers. Without a consistent framework, deteriorating trends can be missed, reviewed late, or explained inconsistently. This project will demonstrate a transparent early-warning and scorecard process that organizes those inputs, applies documented business rules, and highlights issuers that may warrant analyst review. It will support—not automate or replace—human credit judgment.

## Intended users

- Credit analysts monitoring corporate or other non-sovereign issuers
- Portfolio and risk managers reviewing changes in issuer risk
- Students and hiring reviewers evaluating an end-to-end credit-risk portfolio project

The initial implementation will be designed for educational use by a single analyst rather than production deployment.

## In-scope features

- A documented synthetic or public-data schema for issuer, period, and indicator data
- Data ingestion, validation, and reconciliation controls
- Transparent calculation of selected financial and market indicators
- A rule-based issuer scorecard with documented weights, thresholds, and limitations
- Early-warning flags based on levels, trends, and data-quality conditions
- Historical views that show how indicators and flags change over time
- Explanations of score drivers and warning triggers
- A Streamlit interface for filtering issuers and reviewing results
- Automated tests for important business rules and data transformations
- Documentation that teaches the relevant credit concepts and repository design

## Out-of-scope features

- Real lending, trading, underwriting, or investment decisions
- Production credit ratings or investment recommendations
- Automated approval, limit-setting, or portfolio actions
- Claims that a score predicts default without appropriate evidence and validation
- Confidential company, client, employee, or counterparty data
- Personally identifiable or material non-public information
- Paid or restricted datasets that cannot be redistributed in a portfolio
- Production infrastructure, real-time alert delivery, or enterprise integrations
- A black-box model whose outputs cannot be explained and reviewed

## Data privacy boundaries

- Use only clearly labeled synthetic data or data from documented public sources.
- Do not request, store, or process confidential, proprietary, personally identifiable, or material non-public information.
- Record the source, retrieval date, permitted use, and relevant limitations for public datasets.
- Keep credentials and local secrets outside version control.
- Do not imply that synthetic issuers, events, or results describe real entities.
- Review data before publication to ensure that no restricted information is included.

## Initial success criteria

The first usable version will be successful when:

1. A beginner can follow the documentation and explain the business purpose, main data flow, scorecard rules, and limitations.
2. Every included dataset is synthetic or traceable to a documented public source.
3. Source-to-output reconciliation checks identify missing, duplicate, or unexpectedly excluded records.
4. Scorecard calculations and early-warning rules are transparent, reproducible, and covered by tests for important boundaries.
5. The interface allows a user to select an issuer, review current and historical indicators, and understand each displayed warning.
6. Demonstration results are reported honestly, with no fabricated findings or hard-coded outcomes.

These criteria define an educational minimum viable project, not evidence that the system is suitable for real-world credit decisions.
