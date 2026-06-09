<div align="center">

# 💥 BlastRadius

**PR Risk Simulator — Predict the Impact of Your Changes**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://python.org)
[![Analysis](https://img.shields.io/badge/analysis-static-blue.svg)](https://blastradius.io)

*Know exactly what your 3-line change actually touches.*

[Features](#features) • [Quick Start](#quick-start) • [How it Works](#how-it-works) • [GitHub Integration](#github-integration) • [Reviewer Guidance](#reviewer-guidance)

</div>

---

## The Problem

You've been there: you change a "small" helper function, CI goes green, you merge, and **half the system breaks**. 

Traditional static analysis (linters, type checkers) tells you if the code is valid. But they don't tell you the **functional blast radius** of a change.
- Which modules depend on this symbol?
- Which tests are *actually* relevant to this PR?
- Which documentation pages need an update now?
- Who is the best person to review this specific cross-cutting change?

## The Solution

BlastRadius is a **PR risk simulator**. It analyzes your diff against the project's symbol graph to predict exactly what will be affected. It generates a report with evidence, ranks tests by relevance, and suggests the right reviewers based on ownership history.

```bash
# Analyze a PR or local diff
blastradius analyze --branch feat/new-auth

# Output:
# [CRITICAL] Overall Impact: HIGH
# [MODULE]   auth.py (Directly modified)
# [TEST]     tests/test_login.py (Impacted: uses auth.validate_token)
# [DOCS]     docs/authentication.md (Needs update: references changed API)
# [REVIEW]   @rachel (Owner of auth.py), @sam (Modified downstream 3 days ago)
```

## Features

| Feature | Description |
|---------|-------------|
| 📈 **Blast Radius Graph** | Map diffs to symbol dependencies to find hidden impacts |
| 🧪 **Test Ranking** | Know exactly which tests to run first to catch regressions |
| 📖 **Doc Impact Detection** | Identify documentation that needs to change with the code |
| 👥 **Reviewer Guidance** | Smart reviewer recommendations based on code ownership and history |
| 📝 **Checklist Generation** | Auto-generate a custom regression checklist for each PR |
| 🤖 **GitHub App** | Integrate as a PR comment for instant feedback |

## Quick Start

### 1. Install

```bash
pip install blast-radius
```

### 2. Analyze Local Changes

```bash
blastradius analyze .
```

### 3. CI Integration

Add BlastRadius to your GitHub Actions workflow:

```yaml
steps:
  - uses: actions/checkout@v4
  - run: blastradius analyze --format sarif --output blastradius.sarif
  - uses: github/codeql-action/upload-sarif@v2
    with:
      sarif_file: blastradius.sarif
```

## How it Works

1. **Diff-to-Symbol**: Maps the changed lines in your PR to specific functions, classes, and variables.
2. **Graph Traversal**: Uses static analysis (tree-sitter and CodeQL) to follow the dependency chain downstream.
3. **Evidence Extraction**: Links every prediction to the specific line of code that creates the dependency.
4. **Ranking**: Uses historical data and change frequency to rank the risk level of affected modules.

## GitHub Integration

BlastRadius works best as a **GitHub App**. It comments on every PR with a "Risk Summary" that helps maintainers understand the stakes of a change before they even look at the code.

## Reviewer Guidance

Stop tagging "everyone" or the same two people for every PR. BlastRadius identifies the people who have the most context on the **affected areas**, even if they didn't touch the files in this specific PR.

## Built By

BlastRadius is part of the [EmbrOS](https://embros.xyz) toolkit for AI developers.

---

<div align="center">

**Stop merging in the dark. ⭐**

[🌐 embros.xyz](https://embros.xyz)

</div>

---

🐦 Follow on X: [@probert_mihai](https://x.com/probert_mihai)
