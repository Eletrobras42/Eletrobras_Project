@echo off
REM Script para iniciar serviços do Eletrobras Predictive Monitoring

echo 🚀 Iniciando serviços...

echo 📡 Iniciando backend FastAPI na porta 8000...
start "Backend - Eletrobras API" cmd /k "cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak >nul

echo 🌐 Iniciando frontend React na porta 3000...
start "Frontend - Eletrobras Web" cmd /k "cd frontend && npm start"

echo.
echo 🎉 Serviços iniciados!
echo.
echo 📊 Aplicação Eletrobras Predictive Monitoring está rodando:
echo    • Backend API: http://127.0.0.1:8000
echo    • Frontend Web: http://127.0.0.1:3000
echo    • Documentação: http://127.0.0.1:8000/docs
echo.
echo 💡 Feche as janelas dos terminais para parar os serviços.
echo.
pause