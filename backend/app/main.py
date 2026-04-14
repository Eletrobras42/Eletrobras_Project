from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, ALLOWED_ORIGINS
from app.core.database import init_db
from app.services.catalog_service import CatalogService
from app.api.routes.health import router as health_router
from app.api.routes.sources import router as sources_router
from app.api.routes.ingestion import router as ingestion_router
from app.api.routes.indicators import router as indicators_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.anomalies import router as anomalies_router
from app.api.routes.predictions import router as predictions_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    CatalogService.seed_default_sources()
    yield

app = FastAPI(
    title=APP_NAME,
    description="API de ingestão documental, catalogação e dashboard analítico do Eletrobras Predictive Monitoring.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(sources_router)
app.include_router(ingestion_router)
app.include_router(indicators_router)
app.include_router(dashboard_router)
app.include_router(anomalies_router)
app.include_router(predictions_router)
