# Claim Registry

This folder holds the master claim registry for the project.

## Files

- `master_claim_registry.xlsx` — human-editable master workbook with dropdowns, frozen headers, and guidance.
- `master_claim_registry.csv` — machine-readable export for Git version history, scripts, and reproducible analysis.

## Recommended repo location

```text
/registries
  /claims
    master_claim_registry.xlsx
    master_claim_registry.csv
    README.md
```

## Setup steps

1. Open your GitHub repository.
2. Create the folder path `registries/claims/` if it does not already exist.
3. Upload these three files into that folder:
   - `master_claim_registry.xlsx`
   - `master_claim_registry.csv`
   - `README.md`
4. Commit them with a message like:
   - `Add master claim registry`
5. After every meaningful registry update:
   - edit the `.xlsx`
   - export or refresh the `.csv`
   - commit both files together

## Operating rule

The `.xlsx` file is the working master.
The `.csv` file is the audit trail and scripting surface.

Do not treat the CSV as the main editing file unless you are making a deliberate bulk edit in code.

## Row rule

Use one row per claim or one row per operationalized test statement.

Split compound claims into separate rows.

Use `Parent_Claim_ID` to link subclaims and test statements back to a higher-level claim.

## Claim ID rule

Use stable IDs such as:

- `C001` for a core claim
- `C001.1` for a subclaim
- `C001.T1` for a first operational test statement

You can keep the existing `C001`, `C002`, ... starter rows or replace them with your actual IDs.

## Field guide

### Identity and structure
- `Claim_ID` — unique ID for the row
- `Parent_Claim_ID` — parent claim if this row is a child claim or test statement
- `Claim_Level` — suggested values: `Core`, `Subclaim`, `Operational`
- `Claim_Text` — the exact claim in plain language
- `Domain` — domain the claim belongs to

### Readiness and review
- `Status` — suggested flow: `Draft -> Defined -> Testable -> Tested -> Supported / Mixed / Refuted`
- `Priority` — suggested values: `High`, `Medium`, `Low`
- `Falsifiable` — `Yes`, `No`, or `Partial`

### Operationalization
- `Operational_Test_Statement` — the measurable version of the claim
- `Key_Variables_or_Constructs` — variables, constructs, or observables
- `Expected_Direction_or_Mechanism` — predicted relation or mechanism
- `Evidence_Needed` — what evidence would count

### Review and evidence
- `Current_Evidence_Summary` — plain summary of what currently exists
- `Strongest_Supporting_Source` — best support source
- `Strongest_Opposing_Source` — best disconfirming source
- `Method_or_Dataset_to_Test` — planned method or dataset
- `Metric_or_Decision_Rule` — test metric and fail/pass rule
- `Dependencies_or_Assumptions` — dependencies, scope conditions, assumptions
- `Risks_or_Confounds` — likely confounds or failure points

### Ownership and links
- `Owner` — who is responsible
- `Date_Added` — date created
- `Last_Reviewed` — date last reviewed
- `Next_Action` — immediate next step
- `Prereg_Link` — related preregistration
- `Code_Data_Link` — related repository path or dataset path
- `Reset_Memo_Link` — related reset memo
- `Notes` — anything not captured elsewhere

## Minimum workflow

1. Add core claims first.
2. Add subclaims under each core claim.
3. Convert only the strongest subclaims into operational test statements.
4. Do not mark anything `Supported` without a reviewable method, data source, and decision rule.
5. Always include the strongest opposing source when possible.

## Git workflow

Use commit messages like:

- `Add initial core claims`
- `Split bundled claims into separate rows`
- `Add operational test statements for seizure study`
- `Update evidence review for ecology claims`

## Good practice

- Keep claims short and literal.
- Separate symbolic language from empirical language.
- Avoid putting multiple predictions in one row.
- Link every tested row to code, data, and prereg where possible.
- Preserve refuted claims in the registry instead of deleting them.

## First real use

Populate the first five rows with:

1. one top-level project claim
2. one narrower subclaim
3. one operational test statement
4. one disconfirming dependency or assumption
5. one next action tied to a dataset or preregistration
