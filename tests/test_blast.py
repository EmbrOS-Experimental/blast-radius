import pytest
from blastradius.core.models import CodeChange, ImpactLevel
from blastradius.analysis.engine import RiskAnalyzer

def test_risk_analyzer_low_impact():
    analyzer = RiskAnalyzer()
    changes = [
        CodeChange(file_path="utils/helper.py", added_lines=[1, 2], deleted_lines=[])
    ]
    report = analyzer.analyze_changes(changes)
    assert report.overall_impact == ImpactLevel.LOW
    assert len(report.affected_entities) == 2 # helper.py and its test

def test_risk_analyzer_high_impact():
    analyzer = RiskAnalyzer()
    changes = [
        CodeChange(file_path="core/auth.py", added_lines=[1], deleted_lines=[])
    ]
    report = analyzer.analyze_changes(changes)
    assert report.overall_impact == ImpactLevel.HIGH
    assert any(e.name == "core/auth_test.py" for e in report.affected_entities)

def test_suggested_reviewers():
    analyzer = RiskAnalyzer()
    changes = [
        CodeChange(file_path="src/engine/main.py", added_lines=[1], deleted_lines=[])
    ]
    report = analyzer.analyze_changes(changes)
    assert "owner_of_src" in report.suggested_reviewers
