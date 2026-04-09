# Script de Setup Inline - Eletrobras Predictive Monitoring
# Execute com: powershell -ExecutionPolicy Bypass -File setup_inline.ps1

Write-Host "🚀 Iniciando setup automático do Eletrobras Predictive Monitoring..." -ForegroundColor Green

# Função para verificar se comando existe
function Test-Command {
    param ($Command)
    try {
        Get-Command $Command -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

# Verificar Python
Write-Host "📦 Verificando Python..." -ForegroundColor Yellow
if (-not (Test-Command python)) {
    Write-Host "❌ Python não encontrado. Instale Python 3.8+ primeiro." -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

$pythonVersion = python --version 2>&1
Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green

# Verificar Node.js
Write-Host "📦 Verificando Node.js..." -ForegroundColor Yellow
if (-not (Test-Command node)) {
    Write-Host "❌ Node.js não encontrado. Instale Node.js 18+ primeiro." -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

$nodeVersion = node --version
Write-Host "✅ Node.js encontrado: $nodeVersion" -ForegroundColor Green

# Verificar arquivos essenciais
Write-Host "📁 Verificando arquivos essenciais..." -ForegroundColor Yellow
$essentialFiles = @(
    "backend\requirements.txt",
    "backend\app\main.py",
    "frontend\package.json",
    "frontend\src\App.jsx",
    "data\eletrobras_consumo_historico.csv"
)

foreach ($file in $essentialFiles) {
    if (-not (Test-Path $file)) {
        Write-Host "❌ Arquivo essencial não encontrado: $file" -ForegroundColor Red
        Read-Host "Pressione Enter para sair"
        exit 1
    }
}
Write-Host "✅ Todos os arquivos essenciais estão presentes." -ForegroundColor Green

# Instalar dependências do backend
Write-Host "📦 Instalando dependências do backend..." -ForegroundColor Yellow
Push-Location backend
try {
    & python -m pip install --upgrade pip
    & pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Falha ao instalar dependências do backend." -ForegroundColor Red
        Read-Host "Pressione Enter para sair"
        exit 1
    }
    Write-Host "✅ Dependências do backend instaladas." -ForegroundColor Green
} finally {
    Pop-Location
}

# Instalar dependências do frontend
Write-Host "📦 Instalando dependências do frontend..." -ForegroundColor Yellow
Push-Location frontend
try {
    & npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Falha ao instalar dependências do frontend." -ForegroundColor Red
        Read-Host "Pressione Enter para sair"
        exit 1
    }
    Write-Host "✅ Dependências do frontend instaladas." -ForegroundColor Green
} finally {
    Pop-Location
}

# Verificar versões das bibliotecas críticas
Write-Host "🔍 Verificando versões das bibliotecas..." -ForegroundColor Yellow
Push-Location backend
try {
    $fastapiVersion = python -c "import fastapi; print(fastapi.__version__)" 2>$null
    if ($fastapiVersion) {
        Write-Host "✅ FastAPI: $fastapiVersion" -ForegroundColor Green
    }

    $pandasVersion = python -c "import pandas; print(pandas.__version__)" 2>$null
    if ($pandasVersion) {
        Write-Host "✅ Pandas: $pandasVersion" -ForegroundColor Green
    }

    $scikitVersion = python -c "import sklearn; print(sklearn.__version__)" 2>$null
    if ($scikitVersion) {
        Write-Host "✅ Scikit-learn: $scikitVersion" -ForegroundColor Green
    }
} finally {
    Pop-Location
}

Write-Host "" -ForegroundColor White
Write-Host "🎉 Setup concluído!" -ForegroundColor Green
Write-Host "📊 Para iniciar os serviços, execute em terminais separados:" -ForegroundColor White
Write-Host "   • Backend: cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000" -ForegroundColor White
Write-Host "   • Frontend: cd frontend && npm run dev" -ForegroundColor White
Write-Host "" -ForegroundColor White
Write-Host "💡 Ou use o script completo: powershell -ExecutionPolicy Bypass -File setup.ps1" -ForegroundColor Yellow
Write-Host "" -ForegroundColor White
Read-Host "Pressione Enter para sair"