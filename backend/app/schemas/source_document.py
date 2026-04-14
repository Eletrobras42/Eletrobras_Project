from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SourceDocumentResponse(BaseModel):
    id: int
    report_year: int
    document_type: str
    title: str
    source_url: str
    source_page: str
    file_format: str | None = None
    publication_scope: str | None = None
    is_active: int
    discovered_at: datetime
    last_checked_at: datetime | None = None
    notes: str | None = None
    model_config = ConfigDict(from_attributes=True)
