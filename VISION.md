# BlastRadius — Vision

## Elevator Pitch
A **PR risk simulator** that predicts which modules, tests, APIs, docs, and reviewers your change is likely to affect.

## The Problem
CodeQL has AST/control-flow/data-flow. Zoekt and tree-sitter give code structure and search. But there's no maintainer-friendly product layer that converts these into a PR-native "blast radius" report with evidence, test ranking, and reviewer guidance.

## User Stories
1. Developer opens a PR
2. BlastRadius comments: likely affected modules, impacted tests, docs needing updates, likely owners/reviewers, regression checklist
3. Team leads get fast risk summary; maintainers get fewer "looks fine to me" reviews on risky changes

## Core Features
- Diff-to-symbol graph analysis
- Affected module prediction with evidence
- Test impact ranking (which tests to run first)
- Documentation impact detection
- Reviewer recommendation (based on ownership/history)
- SARIF upload for GitHub integration
- GitHub App / PR comment interface

## What Makes It Different
- **PR-native**: integrates as a GitHub App comment
- **Evidence-based**: every prediction links to code
- **Actionable**: test ranking, reviewer suggestions, checklist
- **Static analysis powered**: CodeQL + tree-sitter, not heuristics

## Virality Hooks
- "We predicted this hidden downstream failure before CI went red"
- "What this tiny line change actually touched"
- "BlastRadius found 12 affected modules in a 3-line change"

## License
Apache-2.0

## Monetization
GitHub App subscription, enterprise reviewer routing, compliance rules, historical change-risk analytics
