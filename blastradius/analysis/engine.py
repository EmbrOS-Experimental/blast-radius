from typing import List
from blastradius.core.models import CodeChange, RiskReport, AffectedEntity, ImpactLevel

class RiskAnalyzer:
    def __init__(self, project_path: str = "."):
        self.project_path = project_path

    def analyze_changes(self, changes: List[CodeChange]) -> RiskReport:
        affected_entities = []
        overall_impact = ImpactLevel.LOW
        
        for change in changes:
            # Heuristic: core modules increase impact
            if "core" in change.file_path or "api" in change.file_path:
                overall_impact = ImpactLevel.HIGH
            
            # Heuristic: affected tests
            test_file = change.file_path.replace(".py", "_test.py").replace("src/", "tests/")
            affected_entities.append(AffectedEntity(
                name=change.file_path,
                type="module",
                reason="Directly modified"
            ))
            
            # Simple downstream prediction (simulated)
            if change.file_path.endswith(".py"):
                affected_entities.append(AffectedEntity(
                    name=test_file,
                    type="test",
                    reason="Likely affected test",
                    evidence=f"Module {change.file_path} is modified"
                ))

        summary = f"Analyzed {len(changes)} changed files. Found {len(affected_entities)} potentially affected entities."
        
        return RiskReport(
            summary=summary,
            overall_impact=overall_impact,
            affected_entities=affected_entities,
            suggested_reviewers=["owner_of_" + changes[0].file_path.split("/")[0]],
            regression_checklist=["Verify backward compatibility", "Check for performance regressions"]
        )
