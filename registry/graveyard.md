# Graveyard Registry (Falsified / Not-Supported Claims)

This registry exists so misses can’t be hidden.

**Purpose:** Increase correctability.  
**Not a weapon:** Do not use entries to shame individuals. Audit claims, not people.  
**Integrity rule:** A failed preregistered prediction is logged as **FALSIFIED / NOT SUPPORTED** per its failure rule. Any reinterpretation becomes a **new hypothesis** for future testing.

## Status Legend
- **FALSIFIED** = prereg prediction failed its stated criterion (including reversal)
- **NOT SUPPORTED** = measurement/sampling regime could not resolve the claim (boundary condition added)
- **RETIRED** = claim withdrawn (no longer asserted)

---

## GR-001 — Program A: Fire Ecology Memory Parameter

**Claim ID:** FA.Program_A.H1.v1  
**Tier:** A (preregistered)  
**Program / Domain:** Program A — Fire ecology recovery prediction  
**Prereg text:** Memory parameter Co* improvement ≥ **+5% ΔAUC** in recovery prediction  
**Dataset / window / metric:** MODIS fire scars, Quebec boreal forest, 2013–2020, **monthly cadence**  
**Primary endpoint:** ΔAUC improvement from baseline to Co*-augmented model  
**Failure rule:** ΔAUC < **+5%** threshold  

**Observed result:** baseline AUC **0.714** → Co* AUC **0.730** = **+1.6% ΔAUC**  
**Status:** **FALSIFIED** (failed prereg threshold)

**Costly correction / boundary update:** Monthly cadence is likely too coarse to resolve the proposed “memory” signature; scope narrowed to the sampling regime.  
**What would change my mind next (new risky prediction):** At higher temporal resolution (e.g., weekly/daily proxies), Co* should produce a preregistered improvement that clears a stated threshold on held-out data.  
**Notes:** Exploratory signal `coupling_sync_frac` (+10.44% AUC) treated as **Tier B** hypothesis pending replication.  
**Date logged:** 2026-01-03

---

## GR-002 — Program B: Seizure Approach Compression

**Claim ID:** FA.Program_B.H1_H2.v1  
**Tier:** A (preregistered)  
**Program / Domain:** Program B — Wearable EEG seizure approach dynamics  
**Prereg text:** Seizure approach shows **compression** (var_coh ↓, SD(d) ↓)  
**Dataset / window / metric:** SeizeIT2 wearable EEG, **256 focal seizures**, N=27, 2-channel behind-ear  
**Primary endpoint:** Directional hypotheses: var_coh ↓ and SD(d) ↓ approaching seizure  
**Failure rule:** Direction reversal or null result  

**Observed result:** var_coh **INCREASED** (d≈1.19, p<0.001); SD(d) **INCREASED** (d≈1.32, p<0.001)  
**Status:** **FALSIFIED** (opposite direction observed)

**Costly correction / boundary update:** Mapping revised: “approach” behaves as **expansion / Fracture**, not compression. Any “Return” signature is relocated away from approach and hypothesized for **postictal recovery windows** (new claim, requires new prereg + failure rule).  
**What would change my mind next (new risky prediction):** A preregistered test showing compression/coupling signatures in specifically defined postictal recovery windows (with clear thresholds and baselines).  
**Date logged:** 2026-01-03

---

## GR-003 — Program A: Phase Structure Resolution at Monthly Cadence

**Claim ID:** FA.Program_A.Phase_Structure.v1  
**Tier:** A (preregistered)  
**Program / Domain:** Program A — FIRR phase detectability in fire recovery  
**Prereg text:** FIRR phase structure identifiable at **monthly** temporal resolution in fire recovery  
**Dataset / window / metric:** MODIS fire scars, Quebec boreal forest, 2013–2020, monthly cadence  
**Primary endpoint:** Clear phase transitions (Fracture → Inversion → Recursion → Return)  
**Failure rule:** Phase transitions not resolvable at sampling cadence  

**Observed result:** Phase structure **inconclusive** at monthly resolution  
**Status:** **NOT SUPPORTED** (temporal resolution insufficient)

**Costly correction / boundary update:** Boundary condition added: FIRR mapping requires temporal resolution matched to system dynamics (cadence-dependent claim).  
**What would change my mind next (new risky prediction):** At higher temporal resolution (or alternate data streams with finer cadence), preregistered phase-transition criteria should become detectable if the phase claim is true.  
**Date logged:** 2026-01-03
