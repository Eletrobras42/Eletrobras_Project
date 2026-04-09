@echo off
echo ========================================
echo  🚀 INICIANDO ELETROBRAS BI DASHBOARD
echo ========================================
echo.
set "ROOT_DIR=%~dp0"
cd /d "%ROOT_DIR%"

echo ✅ Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado. Instale Python 3.8+ primeiro.
    pause
    exit /b 1
)

echo ✅ Verificando Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js não encontrado. Instale Node.js 18+ primeiro.
    pause
    exit /b 1
)

echo.
echo 🔧 Instalando dependências do backend...
cd /d "%ROOT_DIR%backend"
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependências do backend
    pause
    exit /b 1
)

echo.
echo 🔧 Instalando dependências do frontend...
cd /d "%ROOT_DIR%frontend"
call npm install
if errorlevel 1 (
    echo ❌ Erro ao instalar dependências do frontend
    pause
    exit /b 1
)

echo.
echo ✅ Dependências instaladas com sucesso!
echo.
echo 🌐 Iniciando servidores...
echo.

echo 📊 Backend (FastAPI) iniciando na porta 8000...
start "Backend Server" cmd /k cd /d "%ROOT_DIR%backend" ^&^& uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

timeout /t 3 /nobreak >nul

echo 🎨 Frontend (React) iniciando na porta 3000...
start "Frontend Server" cmd /k cd /d "%ROOT_DIR%frontend" ^&^& npm run dev

echo.
echo ========================================
echo  🎉 SERVIDORES INICIADOS!
echo ========================================
echo.
echo 📱 Acesse o Dashboard BI:
echo    http://localhost:3000
echo.
echo 📚 API Documentation:
echo    http://localhost:8000/docs
echo.
echo 💡 Navegação:
echo    1. Abra http://localhost:3000
echo    2. Clique em "Dashboard BI"
echo    3. Explore as abas: Visão Executiva, Analytics, Anomalias
echo.
pause