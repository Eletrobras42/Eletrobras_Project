import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.core.database import Base


class IngestionRun(Base):
    __tablename__ = "ingestion_runs"

    id = Column(Integer, primary_key=True, index=True)
    started_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)
    source_document_id = Column(Integer, ForeignKey("source_documents.id"), nullable=True)
    pipeline_version = Column(String, nullable=True)
    rows_extracted = Column(Integer, default=0)
    rows_loaded = Column(Integer, default=0)
    warnings_count = Column(Integer, default=0)
    errors_count = Column(Integer, default=0)
    execution_log = Column(Text, nullable=True)
