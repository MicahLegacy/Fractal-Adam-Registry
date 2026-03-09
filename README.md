# Reproducible repo scaffold

This scaffold separates immutable inputs, scripted transforms, exploratory notebooks, generated outputs, and registry documents.

## Core rules

1. Raw data are immutable once acquired.
2. Processed data must be script-generated.
3. Notebooks are not the source of truth for important logic.
4. Every serious run should record its input manifest, parameters, and commit hash.
5. Each preregistered study should map cleanly to a claim ID and a results subfolder.
