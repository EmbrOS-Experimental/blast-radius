from enum import Enum
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class ImpactLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class AffectedEntity(BaseModel):
    name: str
    type: str # module, function, class, test, doc
    reason: str
    evidence: Optional[str] = None

class RiskReport(BaseModel):
    summary: str
    overall_impact: ImpactLevel
    affected_entities: List[AffectedEntity] = []
    suggested_reviewers: List[str] = []
    regression_checklist: List[str] = []

class CodeChange(BaseModel):
    file_path: str
    added_lines: List[int]
    deleted_lines: List[int]
    changed_symbols: List[str] = []
