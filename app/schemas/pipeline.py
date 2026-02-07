from __future__ import annotations

from pydantic import BaseModel, Field


class Step(BaseModel):
    id: str = Field(..., min_length=1, max_length=64)
    deps: list[str] = Field(default_factory=list)


class PipelineRequest(BaseModel):
    steps: list[Step]


class PipelineReport(BaseModel):
    ok: bool
    errors: list[str]
    mermaid: str
    topo_order: list[str]
