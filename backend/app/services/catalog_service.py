from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.source_document import SourceDocument
from app.repositories.source_repository import SourceDocumentRepository


class CatalogService:
    DEFAULT_SOURCES = [
        {
            "report_year": 2024,
            "document_type": "annual_report",
            "title": "Relatório Anual 2024",
            "source_url": "URL_OFICIAL_2024_RA",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2024,
            "document_type": "executive_summary",
            "title": "Relatório Anual 2024 - Resumo Executivo",
            "source_url": "URL_OFICIAL_2024_RESUMO",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2024,
            "document_type": "html_version",
            "title": "Relatório Anual 2024 - Versão HTML",
            "source_url": "URL_OFICIAL_2024_HTML",
            "source_page": "relatorio-anual",
            "file_format": "html",
            "publication_scope": "public",
        },
        {
            "report_year": 2024,
            "document_type": "base_preparation",
            "title": "Base de Preparação para o Relatório Anual 2024",
            "source_url": "URL_OFICIAL_2024_BASE",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2023,
            "document_type": "annual_report",
            "title": "Relatório Anual 2023",
            "source_url": "URL_OFICIAL_2023_RA",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2023,
            "document_type": "executive_summary",
            "title": "Relatório Anual 2023 - Resumo Executivo",
            "source_url": "URL_OFICIAL_2023_RESUMO",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2023,
            "document_type": "html_version",
            "title": "Relatório Anual 2023 - Versão HTML",
            "source_url": "URL_OFICIAL_2023_HTML",
            "source_page": "relatorio-anual",
            "file_format": "html",
            "publication_scope": "public",
        },
        {
            "report_year": 2023,
            "document_type": "base_preparation",
            "title": "Base de Preparação para o Relatório Anual 2023",
            "source_url": "URL_OFICIAL_2023_BASE",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "annual_report",
            "title": "Relatório Anual 2022",
            "source_url": "URL_OFICIAL_2022_RA",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "executive_summary",
            "title": "Relatório Anual 2022 - Resumo Executivo",
            "source_url": "URL_OFICIAL_2022_RESUMO",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "html_version",
            "title": "Relatório Anual 2022 - Versão HTML",
            "source_url": "URL_OFICIAL_2022_HTML",
            "source_page": "relatorio-anual",
            "file_format": "html",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "sasb_report",
            "title": "Relatório SASB 2022",
            "source_url": "URL_OFICIAL_2022_SASB",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "ods_book",
            "title": "Caderno ODS 2022",
            "source_url": "URL_OFICIAL_2022_ODS",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2022,
            "document_type": "tcfd_report",
            "title": "Relatório TCFD 2022",
            "source_url": "URL_OFICIAL_2022_TCFD",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2021,
            "document_type": "annual_report",
            "title": "Relatório Anual 2021",
            "source_url": "URL_OFICIAL_2021_RA",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2021,
            "document_type": "executive_summary",
            "title": "Relatório Anual 2021 - Resumo Executivo",
            "source_url": "URL_OFICIAL_2021_RESUMO",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2021,
            "document_type": "sasb_report",
            "title": "Relatório SASB 2021",
            "source_url": "URL_OFICIAL_2021_SASB",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2021,
            "document_type": "ods_book",
            "title": "Caderno ODS 2021",
            "source_url": "URL_OFICIAL_2021_ODS",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
        {
            "report_year": 2021,
            "document_type": "tcfd_report",
            "title": "Relatório TCFD 2021",
            "source_url": "URL_OFICIAL_2021_TCFD",
            "source_page": "relatorio-anual",
            "file_format": "pdf",
            "publication_scope": "public",
        },
    ]

    @staticmethod
    def list_sources(db: Session) -> list[SourceDocument]:
        repository = SourceDocumentRepository(db)
        return repository.get_all()

    @staticmethod
    def seed_default_sources(db: Optional[Session] = None) -> list[SourceDocument]:
        internal_session = None
        if db is None:
            internal_session = SessionLocal()
            db = internal_session

        repository = SourceDocumentRepository(db)
        inserted = []

        for source_data in CatalogService.DEFAULT_SOURCES:
            existing = repository.get_by_url(source_data["source_url"])
            if existing:
                inserted.append(existing)
                continue

            document = SourceDocument(
                report_year=source_data["report_year"],
                document_type=source_data["document_type"],
                title=source_data["title"],
                source_url=source_data["source_url"],
                source_page=source_data["source_page"],
                file_format=source_data.get("file_format"),
                publication_scope=source_data.get("publication_scope"),
                discovered_at=datetime.utcnow(),
            )
            repository.create(document)
            inserted.append(document)

        if internal_session is not None:
            internal_session.close()

        return inserted
