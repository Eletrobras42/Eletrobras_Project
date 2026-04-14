from sqlalchemy.orm import Session

from app.models.source_document import SourceDocument
from app.repositories.base_repository import BaseRepository


class SourceDocumentRepository(BaseRepository[SourceDocument]):
    def __init__(self, db: Session):
        super().__init__(db, SourceDocument)

    def get_by_url(self, source_url: str):
        return self.db.query(SourceDocument).filter(SourceDocument.source_url == source_url).first()

    def list_by_year(self, year: int):
        return self.db.query(SourceDocument).filter(SourceDocument.report_year == year).all()
