# Dataset manifest template

This folder holds the reusable dataset manifest for the Fractal Adam registry.

## Files

- `dataset_manifest_template.xlsx` — working master with dropdowns, formatting, and instructions
- `dataset_manifest_template.csv` — Git-friendly mirror for diffs and scripts

## Recommended repo path

```text
data/manifests/
  dataset_manifest_template.xlsx
  dataset_manifest_template.csv
  README.md
```

## Operating rule

- Edit the `.xlsx` file locally.
- Export or overwrite the `.csv` file after each real update.
- Commit both together.

## What one row means

One row should represent one concrete dataset object or split.

Good:
- one downloaded archive
- one processed table
- one train split
- one holdout split

Bad:
- a whole family of unrelated files bundled into one row
- multiple versions of the same dataset collapsed into one row
- vague labels like `ecology data`

## Minimum fields that should never stay blank once a dataset is real

- `Dataset_ID`
- `Dataset_Name`
- `Lifecycle_Status`
- `Claim_IDs`
- `Source_Type`
- `Source_URL_or_DOI`
- `Local_Relative_Path`
- `File_Format`
- `SHA256`
- `Integrity_Status`
- `Preprocessing_Status`
- `QC_Status`
- `Accessibility_Status`

## Column definitions

- `Dataset_ID` — stable ID such as `D001`
- `Dataset_Name` — clear human-readable name
- `Manifest_Version` — metadata version, not the dataset creator’s version unless that is what you are tracking
- `Lifecycle_Status` — draft, active, frozen, deprecated
- `Claim_IDs` — claim registry IDs this dataset informs
- `Study_IDs` — study or prereg IDs that use the dataset
- `Source_Type` — raw, external, simulated, derived, reference
- `Source_Organization` — publisher, lab, consortium, or source owner
- `Source_URL_or_DOI` — reacquisition link or DOI
- `Access_Date` — date you acquired or confirmed access
- `License` — license or terms label
- `Access_Restrictions` — public, internal, licensed, IRB-bound, etc.
- `Citation_Text` — citation text sufficient to reference the source
- `Raw_File_Name` — source filename or archive name
- `Local_Relative_Path` — repo-relative path
- `File_Format` — csv, parquet, xlsx, zip, json, etc.
- `Data_Split` — full, train, validation, test, holdout, other
- `Rows` — row count where meaningful
- `Columns` — column count where meaningful
- `Size_Bytes` — file size
- `SHA256` — integrity hash
- `Integrity_Status` — pending, verified, mismatch, unknown
- `Schema_or_Data_Dictionary_Path` — path to schema or codebook
- `Collection_Method` — download, API pull, scrape, manual curation, simulation, etc.
- `Preprocessing_Status` — raw, external, interim, processed, archived
- `Processing_Script_Path` — script that generated the next-stage artifact
- `QC_Status` — pending, pass, fail, needs review
- `Accessibility_Status` — public, internal, restricted, licensed, embargoed
- `Owner` — who is responsible for the entry
- `Last_Verified_Date` — last integrity or metadata verification
- `Notes` — bounded notes, not a dumping ground

## Hard rules

1. Raw or externally acquired files do not get silently replaced.
2. If the file changes materially, record a new row or version explicitly.
3. Hashes matter. If a file matters for reproducibility, hash it.
4. Processed outputs should point back to source rows through claim/study context and path lineage.
5. Notebooks are not the source of truth for processing logic. Put that in scripts.

## Commit pattern

Use commit messages that describe the real change, for example:

- `Add SeizeIT2 raw dataset manifest row`
- `Register processed fire ecology feature table`
- `Verify hashes for seizure holdout split`
- `Freeze manifest rows for prereg study S003`
