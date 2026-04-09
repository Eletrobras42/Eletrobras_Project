# Eletrobras Predictive Monitoring

Projeto de monitoramento preditivo de consumo energético para Eletrobras, focado em interpolação de dados históricos, detecção de anomalias e persistência com SQLite.

## 🚀 **ACESSO AO DASHBOARD BI**

### **Como acessar o BI:**
1. **Inicie os servidores:**
   ```bash
   # Terminal 1 - Backend
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

   # Terminal 2 - Frontend
   cd frontend
   npm run dev
   ```

2. **Abra no navegador:**
   - **Aplicação Principal:** http://localhost:3000
   - **API Backend:** http://localhost:8000/docs (Swagger UI)

3. **Navegue para o BI:**
   - Na aplicação principal, clique no botão **"Dashboard BI"**
   - Ou acesse diretamente: http://localhost:3000/dashboard

### **Funcionalidades do BI:**

#### 📊 **Visão Executiva**
- **KPIs em Tempo Real:**
  - Máquinas monitoradas
  - Total de registros
  - Consumo médio (kWh)
  - Taxa de tolerância (%)
- **Gráficos Interativos:**
  - Consumo médio por mês
  - Distribuição por máquina

#### 🔍 **Analytics**
- Análise detalhada por máquina
- Métricas de performance
- Tendências de consumo

#### ⚠️ **Anomalias**
- Detecção automática de anomalias
- Tabela de previsões com alertas
- Taxa de anomalia em tempo real

### **APIs do BI Disponíveis:**
- `GET /api/overview` - Visão geral com KPIs
- `GET /api/timeline` - Dados temporais para gráficos
- `GET /api/machines` - Lista de máquinas monitoradas
- `GET /api/predictions` - Histórico de previsões
- `GET /api/analytics?machine={nome}` - Analytics por máquina

### **Inicialização Rápida:**
Para iniciar automaticamente frontend e backend:
```cmd
iniciar_bi.bat
```

Este script irá:
- ✅ Verificar dependências (Python, Node.js)
- ✅ Instalar bibliotecas automaticamente
- ✅ Iniciar backend (porta 8000)
- ✅ Iniciar frontend (porta 3000)
- ✅ Abrir instruções de acesso

## Estrutura do projeto

- `backend/`
  - `app/main.py`: ponto de entrada da API FastAPI
  - `app/routes/predict.py`: rotas `/api/predict` e `/api/history`
  - `app/routes/analytics.py`: rotas `/api/machines`, `/api/analytics` e `/api/predictions`
  - `app/services/`: lógica de interpolação, predição, métricas e análises
  - `app/models/`: modelos SQLAlchemy para `sensor_data` e `prediction_logs`
  - `app/database/`: conexão SQLite e carga inicial a partir do CSV
  - `app/utils/`: utilitários para ler CSV e suportar dados adicionais
- `frontend/`
  - `src/App.jsx`: formulário do usuário e exibição da previsão
  - `src/components/`: componentes React para entrada e resultado
  - `src/services/api.js`: integração com a API FastAPI
- `data/`
  - `eletrobras_consumo_historico.csv`: base histórica simulada com várias máquinas

## Como executar

### Opção 1: Setup Automático Completo (PowerShell)
Se a política de execução permitir:
```powershell
.\setup.ps1
```

Ou force a execução:
```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

### Opção 2: Setup Simples (Batch) - RECOMENDADO
Execute o script batch que verifica dependências e instala bibliotecas:
```cmd
setup.bat
```

Este script:
- ✅ Verifica Python e Node.js
- ✅ Confirma arquivos essenciais
- ✅ Instala dependências automaticamente
- ✅ Valida versões das bibliotecas

### Opção 3: Setup Inline (PowerShell)
Para sistemas com restrições:
```powershell
powershell -ExecutionPolicy Bypass -File setup_inline.ps1
```

### Após o Setup: Iniciar Serviços
Após executar o setup.bat, inicie os serviços:

```cmd
start_services.bat
```

Este comando abre duas janelas separadas:
- Uma para o backend FastAPI (porta 8000)
- Uma para o frontend React (porta 3000)

**Acesse:**
- Frontend: `http://127.0.0.1:3000`
- Backend API: `http://127.0.0.1:8000`
- Documentação: `http://127.0.0.1:8000/docs`

## Endpoints principais

- `POST /api/predict`
- `GET /api/history?machine=NomeDaMáquina`
- `GET /api/machines`
- `GET /api/analytics?machine=NomeDaMáquina`
- `GET /api/predictions`
- `GET /api/overview`
- `GET /api/timeline`
- `GET /api/export/sensor-data`
- `GET /api/export/predictions`

## Arquivos importantes

- `setup.bat`: Script de verificação e instalação de dependências
- `start_services.bat`: Script para iniciar backend e frontend
- `setup.ps1`: Script PowerShell completo (requer política de execução)
- `setup_inline.ps1`: Script PowerShell inline
- `powerbi/dashboard_design.md`: Guia de design para Power BI com layout e métricas inspiradas nos exemplos
- `.gitignore`: Arquivos ignorados pelo Git

## Próximos passos

- Concluir o front-end React para permitir envio de máquina, tempo e tempo de atividade do colaborador.
- Usar `/api/analytics` para alimentar um dashboard com consumo, anomalias e taxa de tolerância.
- Conectar o Power BI ao banco de dados para criar gráficos de consumo por máquina, evolução temporal e pontos de anomalia.
- Expandir a base de dados com mais métricas publicadas pela Eletrobras e campos adicionais no CSV.
