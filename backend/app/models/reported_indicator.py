import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from app.core.database import Base


class ReportedIndicator(Base):
    __tablename__ = "reported_indicators"

    id = Column(Integer, primary_key=True, index=True)
    source_document_id = Column(Integer, ForeignKey("source_documents.id"), nullable=False)
    ingestion_run_id = Column(Integer, ForeignKey("ingestion_runs.id"), nullable=True)
    report_year = Column(Integer, nullable=False, index=True)
    indicator_code = Column(String, nullable=True)
    indicator_name = Column(String, nullable=False)
    indicator_category = Column(String, nullable=True)
    metric_unit = Column(String, nullable=True)
    raw_value_text = Column(Text, nullable=True)
    numeric_value = Column(Float, nullable=True)
    comparative_period = Column(String, nullable=True)
    business_area = Column(String, nullable=True)
    asset_name = Column(String, nullable=True)
    geography = Column(String, nullable=True)
    source_page_reference = Column(String, nullable=True)
    extraction_confidence = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
