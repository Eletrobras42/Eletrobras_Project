from pydantic import BaseModel, ConfigDict


class IngestionRunRequest(BaseModel):
    source_document_id: int


class IngestionRunResponse(BaseModel):
    id: int
    started_at: str
    finished_at: str | None = None
    status: str
    source_document_id: int | None = None
    pipeline_version: str | None = None
    rows_extracted: int
    rows_loaded: int
    warnings_count: int
    errors_count: int
    execution_log: str | None = None
    model_config = ConfigDict(from_attributes=True)
