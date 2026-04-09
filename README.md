# Eletrobras_Project
Projeto de monitoramento preditivo de consumo energético com backend em FastAPI e frontend em React + Vite.

## Repositório GitHub
- https://github.com/Eletrobras42/Eletrobras_Project

## Visão geral
Este projeto contém:
- `backend/` — API FastAPI com endpoints de previsão, analytics e exportação.
- `frontend/` — Aplicação React usando Vite para exibir dashboards e formulários.
- `data/` — Base histórica de consumo para carga inicial.
- `setup.bat` / `start_services.bat` — scripts para iniciar o ambiente local no Windows.

## Publicação no GitHub
O repositório já está configurado e publicado no GitHub correto.
A branch `main` está rastreando `origin/main`.

### Como enviar mudanças
```powershell
cd C:\Users\Nitro\Downloads\Eletrobras_Project
git add .
git commit -m "Mensagem do commit"
git push
```

## Executando localmente
### Backend
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```cmd
cd frontend
npm install
npm run dev
```

### Acessar
- Frontend: `http://localhost:3000`
- Backend Swagger: `http://localhost:8000/docs`

## Build de produção
### Frontend
```cmd
cd frontend
npm run build
```

### Backend
```powershell
cd backend
python -m compileall app
```

## CI/CD
Há um workflow do GitHub Actions em `.github/workflows/ci.yml` que:
- instala dependências Python e Node
- valida a sintaxe do backend
- gera o build do frontend

## Observações de ambiente Windows
Se o PowerShell bloquear `npm.ps1`, use:
```powershell
cmd /c "npm install"
cmd /c "npm run build"
```

Se o Windows bloquear DLLs do NumPy, pode ser necessário ajustar a política de execução ou usar um ambiente virtual limpo.
