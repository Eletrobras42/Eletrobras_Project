# Script de Setup Automático - Eletrobras Predictive Monitoring
# Este script verifica dependências, instala bibliotecas e inicia os serviços locais

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
    exit 1
}

$pythonVersion = python --version 2>&1
Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green

# Verificar Node.js
Write-Host "📦 Verificando Node.js..." -ForegroundColor Yellow
if (-not (Test-Command node)) {
    Write-Host "❌ Node.js não encontrado. Instale Node.js 18+ primeiro." -ForegroundColor Red
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
    } else {
        Write-Host "⚠️  FastAPI não encontrado após instalação." -ForegroundColor Yellow
    }

    $pandasVersion = python -c "import pandas; print(pandas.__version__)" 2>$null
    if ($pandasVersion) {
        Write-Host "✅ Pandas: $pandasVersion" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Pandas não encontrado após instalação." -ForegroundColor Yellow
    }

    $scikitVersion = python -c "import sklearn; print(sklearn.__version__)" 2>$null
    if ($scikitVersion) {
        Write-Host "✅ Scikit-learn: $scikitVersion" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Scikit-learn não encontrado após instalação." -ForegroundColor Yellow
    }
} finally {
    Pop-Location
}

# Verificar se portas estão livres
Write-Host "🔌 Verificando disponibilidade de portas..." -ForegroundColor Yellow
$backendPort = 8000
$frontendPort = 3000

$backendPortInUse = Get-NetTCPConnection -LocalPort $backendPort -ErrorAction SilentlyContinue
if ($backendPortInUse) {
    Write-Host "⚠️  Porta $backendPort (backend) já está em uso. Verifique se há outro processo rodando." -ForegroundColor Yellow
} else {
    Write-Host "✅ Porta $backendPort (backend) está disponível." -ForegroundColor Green
}

$frontendPortInUse = Get-NetTCPConnection -LocalPort $frontendPort -ErrorAction SilentlyContinue
if ($frontendPortInUse) {
    Write-Host "⚠️  Porta $frontendPort (frontend) já está em uso. Verifique se há outro processo rodando." -ForegroundColor Yellow
} else {
    Write-Host "✅ Porta $frontendPort (frontend) está disponível." -ForegroundColor Green
}

# Iniciar serviços
Write-Host "🚀 Iniciando serviços..." -ForegroundColor Yellow

# Iniciar backend em background
Write-Host "📡 Iniciando backend (FastAPI) na porta $backendPort..." -ForegroundColor Cyan
$backendJob = Start-Job -ScriptBlock {
    param($backendPath)
    Push-Location $backendPath
    try {
        & uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    } finally {
        Pop-Location
    }
} -ArgumentList (Join-Path $PSScriptRoot "backend")

# Aguardar um pouco para o backend iniciar
Start-Sleep -Seconds 3

# Verificar se backend iniciou
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:$backendPort/health" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ Backend iniciado com sucesso! Acesse: http://127.0.0.1:$backendPort" -ForegroundColor Green
    Write-Host "📖 Documentação da API: http://127.0.0.1:$backendPort/docs" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Backend pode não ter iniciado corretamente. Verifique os logs." -ForegroundColor Yellow
}

# Iniciar frontend em background
Write-Host "🌐 Iniciando frontend (React) na porta $frontendPort..." -ForegroundColor Cyan
$frontendJob = Start-Job -ScriptBlock {
    param($frontendPath)
    Push-Location $frontendPath
    try {
        & npm run dev
    } finally {
        Pop-Location
    }
} -ArgumentList (Join-Path $PSScriptRoot "frontend")

# Aguardar um pouco para o frontend iniciar
Start-Sleep -Seconds 5

# Verificar se frontend iniciou
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:$frontendPort" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ Frontend iniciado com sucesso! Acesse: http://127.0.0.1:$frontendPort" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Frontend pode não ter iniciado corretamente. Verifique os logs." -ForegroundColor Yellow
}

Write-Host "" -ForegroundColor White
Write-Host "🎉 Setup concluído!" -ForegroundColor Green
Write-Host "📊 Aplicação Eletrobras Predictive Monitoring está rodando:" -ForegroundColor White
Write-Host "   • Backend API: http://127.0.0.1:$backendPort" -ForegroundColor White
Write-Host "   • Frontend Web: http://127.0.0.1:$frontendPort" -ForegroundColor White
Write-Host "   • Documentação: http://127.0.0.1:$backendPort/docs" -ForegroundColor White
Write-Host "" -ForegroundColor White
Write-Host "💡 Para parar os serviços, feche este terminal ou pressione Ctrl+C." -ForegroundColor Yellow
Write-Host "🔄 Execute este script novamente sempre que editar o código." -ForegroundColor Yellow

# Manter o script rodando para manter os jobs ativos
try {
    while ($true) {
        Start-Sleep -Seconds 1
    }
} finally {
    # Cleanup quando o script for interrompido
    Write-Host "🛑 Parando serviços..." -ForegroundColor Yellow
    Stop-Job $backendJob -ErrorAction SilentlyContinue
    Stop-Job $frontendJob -ErrorAction SilentlyContinue
    Remove-Job $backendJob -ErrorAction SilentlyContinue
    Remove-Job $frontendJob -ErrorAction SilentlyContinue
    Write-Host "✅ Serviços parados." -ForegroundColor Green
}