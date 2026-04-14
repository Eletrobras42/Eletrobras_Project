@echo off
REM Script de Setup Automático - Eletrobras Predictive Monitoring
REM Este script verifica dependências, instala bibliotecas e inicia os serviços locais

echo 🚀 Iniciando setup automático do Eletrobras Predictive Monitoring...

REM Verificar Python
echo 📦 Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Instale Python 3.8+ primeiro.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✅ Python encontrado: %python_version%

REM Verificar Node.js
echo 📦 Verificando Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js não encontrado. Instale Node.js 18+ primeiro.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('node --version') do set node_version=%%i
echo ✅ Node.js encontrado: %node_version%

REM Verificar arquivos essenciais
echo 📁 Verificando arquivos essenciais...
set "essential_files=backend\requirements.txt backend\app\main.py frontend\package.json frontend\src\App.jsx data\eletrobras_consumo_historico.csv"

for %%f in (%essential_files%) do (
    if not exist "%%f" (
        echo ❌ Arquivo essencial não encontrado: %%f
        pause
        exit /b 1
    )
)
echo ✅ Todos os arquivos essenciais estão presentes.

REM Instalar dependências do backend
echo 📦 Instalando dependências do backend...
cd backend
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Falha ao instalar dependências do backend.
    cd ..
    pause
    exit /b 1
)
echo ✅ Dependências do backend instaladas.
cd ..

REM Instalar dependências do frontend
echo 📦 Instalando dependências do frontend...
cd frontend
cmd /c npm install
if %errorlevel% neq 0 (
    echo ❌ Falha ao instalar dependências do frontend.
    cd ..
    pause
    exit /b 1
)
echo ✅ Dependências do frontend instaladas.
cd ..

REM Verificar versões das bibliotecas críticas
echo 🔍 Verificando versões das bibliotecas...
cd backend
python -c "import fastapi; print('FastAPI:', fastapi.__version__)" 2>nul
python -c "import pandas; print('Pandas:', pandas.__version__)" 2>nul
python -c "import sklearn; print('Scikit-learn:', sklearn.__version__)" 2>nul
cd ..

echo.
echo 🎉 Setup concluído com sucesso!
echo.
echo 📊 Para iniciar os serviços, execute:
echo    • Backend: cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
echo    • Frontend: cd frontend && npm start
echo.
echo 💡 Ou use o script PowerShell: .\setup.ps1 (se a política de execução permitir)
echo.
pause