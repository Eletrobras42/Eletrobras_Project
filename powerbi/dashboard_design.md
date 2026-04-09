# Power BI Dashboard - Eletrobras Predictive Monitoring

## Objetivo
Criar um dashboard que combine visual moderno e analítico, inspirado nos exemplos fornecidos, com foco em:
- apresentação executiva de consumo energético
- indicadores de desempenho (KPIs)
- análise temporal
- detecção de anomalias
- visões por máquina / linha de produção
- competência de operação (tempo de atividade do colaborador)

## Estrutura de páginas sugerida

### Página 1: Visão Executiva de Consumo
- Header com nome do projeto e filtro de período (ano / mês)
- KPIs principais:
  - Consumo total estimado
  - Consumo médio por máquina
  - Taxa média de tolerância
  - Total de anomalias detectadas
- Cartões adicionais:
  - Eficiência de produção
  - Tempo médio de atividade de colaborador
  - Quantidade de previsões realizadas
- Gráfico de linha/área:
  - Consumo estimado por período (mês)
  - Comparação com consumo histórico real
- Gráfico de rosca/barras:
  - Distribuição de consumo por máquina
  - Participação em % por máquina

### Página 2: Análise de Anomalias e Qualidade
- Mapa de calor ou linha de séries temporais:
  - Anomalias por data
- Cartões de status:
  - Previsões fora da tolerância
  - Previsões anômalas
  - Precisão média do modelo
- Tabela de eventos:
  - Máquina
  - Tempo solicitado
  - Consumo estimado
  - Erro percentual
  - Fora da tolerância
  - Anomalia

### Página 3: Operação da Linha e Tempo de Colaborador
- Gráfico de barras:
  - Tempo de atividade por linha/máquina
  - Número de registros por colaborador (se disponível)
- Indicadores de desempenho operacional:
  - Consumo por hora de produção
  - Produtividade estimada
  - Eficiência de produção
- Visão de status por linha de produção:
  - normal / anomalia / fora da tolerância

## Dados necessários no modelo
- `machine_name`
- `timestamp_min`
- `consumo_kwh`
- `temperatura`
- `producao_hora`
- `worker_activity_min`
- `status`
- `predicted_consumo_kwh`
- `erro_percentual`
- `fora_tolerancia`
- `anomalia`
- `created_at`

## Layout e estética
- Fundo escuro com gradientes suaves e paleta neons / corporate blue
- Cards de KPI com bordas arredondadas
- Barras e linhas com cores vibrantes: azul, verde, laranja, roxo
- Tipografia grande e clara para KPIs principais
- Indicadores em destaque no topo, com valores em negrito
- Uso de ícones simples para cada métrica principal

## Mapeamento dos exemplos
- Painel de KPI no topo — semelhante aos exemplos de vendas
- Gráfico de evolução temporal grande no centro
- Distribuição lateral por máquina (barra horizontal)
- Filtros laterais / topo para ano, mês, máquina
- Cards estilizados com métricas principais e variação percentual

## Conexão com o backend
Utilize os seguintes endpoints para alimentar o modelo de dados:
- `GET /api/machines`
- `GET /api/history?machine={machine}`
- `GET /api/analytics?machine={machine}`
- `GET /api/predictions`
- `GET /api/overview`
- `GET /api/timeline`

## Próximo passo
1. Criar o modelo no Power BI Desktop usando o CSV e as APIs para consulta.
2. Construir as medidas DAX para KPIs e taxa de anomalia.
3. Montar as páginas seguindo a estrutura acima.
4. Ajustar cores e typografia para o visual escuro e moderno.
