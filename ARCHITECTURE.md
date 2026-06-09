# BlastRadius — Architecture

## Stack
- **Analysis Engine**: Python orchestrating CodeQL + tree-sitter
- **Graph/Index Store**: Local graph DB or SQLite
- **Interface**: GitHub App comment + SARIF upload
- **CodeQL**: Leverage existing CodeQL databases (GitHub hosts them for public repos)

## Data Flow
```
GitHub PR → Webhook → Python Analyzer
                           ↓
                     CodeQL + tree-sitter
                           ↓
                     Diff → Symbol Graph
                           ↓
              Affected Modules / Tests / Docs / Owners
                           ↓
              GitHub Comment + SARIF Upload
```

## MVP Scope (3–4.5 PM solo, 5.5–7 PM team of 3)
1. Diff-to-symbol graph extraction
2. Affected test prediction
3. PR annotation via GitHub comment

## Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| False confidence | Show confidence scores, always link evidence |
| Static analysis limits | Start with ecosystems that have good dependency metadata |
| Complex monorepos | Phase 2: workspace-aware analysis |
