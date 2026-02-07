from __future__ import annotations

from fastapi import APIRouter

from app.schemas.pipeline import PipelineRequest, PipelineReport
from app.services.pipeline import inspect_pipeline

router = APIRouter(prefix='/pipeline')


@router.post('/inspect', response_model=PipelineReport)
def inspect(req: PipelineRequest) -> PipelineReport:
    rep = inspect_pipeline([s.model_dump() for s in req.steps])
    return PipelineReport(**rep)
