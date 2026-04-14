# Eletrobras Predictive Monitoring
Plataforma de monitoramento preditivo de consumo energético baseada em documentos públicos da Eletrobras.

## Visão geral
Este monorepo segue o Manual Mestre do projeto:
- `backend/` — API FastAPI com modelagem SQLite, ingestão documental, catalogação de fontes, interpolação e detecção de anomalias.
- `frontend/` — Dashboard React com bundler Webpack, interface dark premium e visual executivo.
- `docs/` — documentação técnica de arquitetura, governança e APIs.
- `scripts/` — comandos de execução e inicialização do ambiente.

## Fonte oficial dos dados
O sistema foi projetado para usar como fonte primária os documentos públicos listados na página de Relatório Anual da Eletrobras.
A ideia é catalogar cada documento por ano, tipo, URL de origem e manter rastreabilidade total.

## Stack
### Backend
- FastAPI
- Uvicorn
- Pandas
- SciPy
- scikit-learn
- SQLAlchemy
- Pydantic
- NumPy
- python-dotenv
- typing-extensions

### Frontend
- React
- Webpack

### Banco
- SQLite

```

### Frontend
```powershell
cd frontend
npm install
npm start
```

## Endpoints principais
- `GET /health`
- `GET /sources`
- `POST /sources/seed`
- `POST /ingestion/run`
- `GET /indicators`
- `GET /indicators/series`
- `GET /dashboard/kpis`
- `GET /dashboard/trends`
- `GET /dashboard/anomalies`
- `POST /predictions/interpolate`

## Estrutura do monorepo
- `backend/`
- `frontend/`
- `docs/`
- `scripts/`
