from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIRS = [
    "data/raw",
    "data/external",
    "data/interim",
    "data/processed",
    "data/manifests",
    "src",
    "tests",
    "notebooks",
    "scripts",
    "results/figures",
    "results/tables",
    "results/logs",
    "env",
    "docs/methods",
    "registry/prereg",
]

README_CONTENT = {
    "data/raw/README.md": "# raw\n\nImmutable source data. Never hand-edit files in this folder after acquisition. Record source, version, access date, checksum, and license in the dataset manifest.\n",
    "data/external/README.md": "# external\n\nThird-party reference files that are not the primary study dataset. Store source notes and version information in the dataset manifest.\n",
    "data/interim/README.md": "# interim\n\nTemporary transformation outputs. These can be regenerated. Do not treat this folder as the final analysis input.\n",
    "data/processed/README.md": "# processed\n\nAnalysis-ready inputs produced from raw or external data by scripted steps. Every file here should be reproducible from code plus manifest metadata.\n",
    "data/manifests/README.md": "# manifests\n\nDataset manifests live here. One manifest per dataset or per frozen study input.\n",
    "src/README.md": "# src\n\nReusable project code. Put logic here, not in notebooks. Keep functions small, path handling relative to the repo root, and avoid hard-coded machine-specific locations.\n",
    "tests/README.md": "# tests\n\nMinimal checks for loaders, transforms, and metric calculations. Reproducibility without checks is fragile.\n",
    "notebooks/README.md": "# notebooks\n\nExploration only. Once an analysis matters, move the real logic into src/ or scripts/ and leave the notebook as a report or sanity-check surface.\n",
    "scripts/README.md": "# scripts\n\nThin run scripts that call code from src/. Each serious run should log parameters, input manifest ID, and commit hash.\n",
    "results/figures/README.md": "# figures\n\nGenerated figures. Prefer one study subfolder per preregistered run.\n",
    "results/tables/README.md": "# tables\n\nGenerated tables and exported summaries tied to a specific run or study.\n",
    "results/logs/README.md": "# logs\n\nRun logs, diagnostics, and execution records. These are usually not tracked except for small human-readable summaries.\n",
    "env/README.md": "# env\n\nEnvironment specifications live here. Freeze package versions before any serious preregistered run.\n",
    "docs/README.md": "# docs\n\nProject-facing documentation, decision notes, and methods summaries.\n",
    "docs/methods/README.md": "# methods\n\nMethod notes that explain datasets, transforms, metrics, exclusions, and failure points in plain language.\n",
    "registry/README.md": "# registry\n\nClaim registry, prereg masters, and related audit-control artifacts.\n",
    "registry/prereg/README.md": "# prereg\n\nStore the reusable prereg master here, then duplicate it per study. Finalized preregs should be tied to a commit hash.\n",
}

TOP_LEVEL_README = """# Reproducible repo scaffold\n\nThis scaffold separates immutable inputs, scripted transforms, exploratory notebooks, generated outputs, and registry documents.\n\n## Rules\n\n1. Raw data are immutable once acquired.\n2. Processed data must be script-generated.\n3. Notebooks are not the source of truth for important logic.\n4. Every serious run should record its input manifest, parameters, and commit hash.\n5. Each preregistered study should map cleanly to a claim ID and a results subfolder.\n"""

REQS = """# Minimal scientific Python starter stack\nnumpy\npandas\nscipy\nmatplotlib\njupyter\nnotebook\npyyaml\nopenpyxl\nscikit-learn\n"""

ENV_YML = """name: fractal-adam-repro\nchannels:\n  - conda-forge\ndependencies:\n  - python=3.11\n  - numpy\n  - pandas\n  - scipy\n  - matplotlib\n  - jupyterlab\n  - notebook\n  - pyyaml\n  - openpyxl\n  - scikit-learn\n  - pip\n"""

for rel in DIRS:
    path = ROOT / rel
    path.mkdir(parents=True, exist_ok=True)
    (path / ".gitkeep").touch(exist_ok=True)

for rel, content in README_CONTENT.items():
    path = ROOT / rel
    if not path.exists():
        path.write_text(content, encoding="utf-8")

(ROOT / "README.md").write_text(TOP_LEVEL_README, encoding="utf-8")
(ROOT / "env" / "requirements.txt").write_text(REQS, encoding="utf-8")
(ROOT / "env" / "environment.yml").write_text(ENV_YML, encoding="utf-8")

print("Repo scaffold verified at", ROOT)
