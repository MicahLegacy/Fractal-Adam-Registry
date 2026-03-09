# Fractal Adam Reset Memo

**Version 1 internal reset | 2026-03-09**

## Purpose

This memo resets the project from broad theory presentation to disciplined claim-by-claim empirical work.
The objective is not to defend Fractal Adam as a universal law. The objective is to determine, by bounded tests and transparent failure handling, which parts survive contact with data.

## What is being reset

- Universal framing is no longer the operational center of the project.
- Symbolic, theological, and philosophical material is no longer treated as evidence for empirical claims.
- Cross-domain resemblance is no longer treated as confirmation.
- Rhetorical coherence is no longer treated as scientific progress.
- Notebook experiments are no longer treated as durable results unless they are tied to registered claims, fixed inputs, versioned code, and reproducible outputs.

## What remains in scope

- Bounded claims that can be written clearly, linked to a registry ID, and exposed to possible failure.
- Reusable infrastructure for preregistration, dataset tracking, code versioning, and results logging.
- Exploratory work only when it is clearly labeled as exploratory and separated from confirmatory claims.
- Symbolic or philosophical work only when it is explicitly quarantined from empirical inference.

## Operating rules going forward

- Every serious study starts from a claim ID in the master claim registry.
- Every claim must state what would count against it.
- Every dataset used in analysis must appear in a dataset manifest.
- Every preregistered study must point to a fixed dataset, a fixed analysis plan, and a fixed repo state.
- Raw data are immutable once acquired.
- Processed data must be script-generated.
- Important logic belongs in versioned scripts, not only in notebooks.
- Each results folder must record inputs, parameters, outputs, and commit hash.
- Negative results are retained. Failed claims move to the graveyard instead of being silently reworded.

## Default study ladder

- Claim registry entry
- Dataset manifest entry
- Study-specific prereg copied from the reusable template
- Scripted analysis in the repo scaffold
- Results log tied back to claim ID
- Decision: supported, mixed, inconclusive, or falsified

## Non-goals for Version 1

- No attempt to prove a grand unified theory.
- No claim that one pattern governs all domains.
- No use of aesthetic resonance, sacred imagery, or interpretive depth as empirical support.
- No expansion of scope during analysis to preserve a preferred conclusion.

## Immediate repository anchors

- `registry/claims/` holds the master claim registry.
- `registry/prereg/` holds the reusable template and study-specific preregistrations.
- `data/manifests/` holds dataset manifests.
- `src/`, `scripts/`, `notebooks/`, `results/`, and `tests/` hold the executable research workflow.

## Decision standard

- A claim advances only when the evidence path is transparent, reproducible, and domain-bounded.
- If a claim cannot be operationalized, it does not enter the empirical lane.
- If a result depends on reinterpretation after failure, the claim is not yet ready.

## Bottom line

The reset is from worldview defense to research discipline.
The project earns credibility only by surviving loss, constraint, and external inspection.
