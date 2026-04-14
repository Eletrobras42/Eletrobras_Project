import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base


class SourceDocument(Base):
    __tablename__ = "source_documents"

    id = Column(Integer, primary_key=True, index=True)
    report_year = Column(Integer, nullable=False, index=True)
    document_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    source_url = Column(String, nullable=False, unique=True)
    source_page = Column(String, nullable=False)
    file_format = Column(String, nullable=True)
    publication_scope = Column(String, nullable=True)
    is_active = Column(Integer, nullable=False, default=1)
    discovered_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    last_checked_at = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
