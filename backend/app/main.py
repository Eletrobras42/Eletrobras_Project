from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router
from app.routes.analytics import router as analytics_router
from app.routes.dashboard import router as dashboard_router
from app.routes.export import router as export_router
from app.database.connection import init_db
from app.database.seed import seed_initial_data

app = FastAPI(
    title="Eletrobras Predictive Monitoring API",
    description="API de ingestão e previsão de consumo energético para Eletrobras usando interpolação e análise de dados históricos.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()
    seed_initial_data()

app.include_router(predict_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")
app.include_router(dashboard_router, prefix="/api")
app.include_router(export_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok", "service": "eletrobras-predictive-monitoring"}
