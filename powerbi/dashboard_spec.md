# Power BI Dashboard - Spec de Implementação

## Objetivo
Construir um dashboard com visual moderno, escuro e analítico, inspirado nos exemplos enviados, para monitorar consumo energético, desempenho de produção e anomalias.

## Estrutura do relatório

### Página 1: Visão Executiva
- Topo com título e filtros:
  - Ano
  - Mês
  - Máquina / Linha de produção
- KPIs principais:
  - Consumo Total Estimado
  - Consumo Médio por Máquina
  - Taxa de Tolerância (%)
  - Total de Anomalias
  - Eficiência de Produção
  - Previsões Realizadas
- Gráfico de linha/área:
  - Consumo médio por mês
  - Consumo real x estimado
- Gráfico de rosca ou barras:
  - Consumo por máquina
  - Participação relativa de cada linha

### Página 2: Análise de Qualidade e Anomalias
- KPIs de qualidade:
  - % Anomalias
  - % Previsões fora da tolerância
  - Erro médio
- Gráfico de linha de tendência de anomalias por mês
- Tabela / matriz:
  - Máquina
  - Tempo informado
  - Consumo estimado
  - Erro percentual
  - Fora da tolerância
  - Anomalia

### Página 3: Operação de Linha e Colaborador
- Cartões de operação:
  - Tempo médio de atividade do colaborador
  - Produção média por hora
  - Eficiência de produção por máquina
- Gráfico de barras horizontais:
  - Consumo por máquina
  - Tempo de atividade por máquina
- Gráfico de colunas:
  - Produção por hora vs. consumo

## Modelo de dados
- `SensorData`
  - machine_name
  - timestamp_min
  - consumo_kwh
  - temperatura
  - producao_hora
  - worker_activity_min
  - status
  - created_at
- `PredictionLog`
  - machine_name
  - timestamp_min
  - predicted_consumo_kwh
  - erro_percentual
  - fora_tolerancia
  - anomalia
  - created_at

### Relations
- Relacionar `SensorData[machine_name]` com `PredictionLog[machine_name]`
- Criar tabela de datas a partir de `created_at` e, se necessário, de `timestamp_min`

## Medidas DAX recomendadas

### Consumo
```dax
Total Consumo = SUM(SensorData[consumo_kwh])
```

### Consumo médio
```dax
Consumo Médio = AVERAGE(SensorData[consumo_kwh])
```

### Previsões realizadas
```dax
Previsões Realizadas = COUNTROWS(PredictionLog)
```

### Taxa de tolerância
```dax
Taxa de Tolerância =
DIVIDE(
    CALCULATE(COUNTROWS(PredictionLog), PredictionLog[fora_tolerancia] = FALSE),
    COUNTROWS(PredictionLog),
    0
)
```

### Taxa de anomalia
```dax
Taxa de Anomalia =
DIVIDE(
    CALCULATE(COUNTROWS(PredictionLog), PredictionLog[anomalia] = TRUE),
    COUNTROWS(PredictionLog),
    0
)
```

### Erro médio
```dax
Erro Médio = AVERAGE(PredictionLog[erro_percentual])
```

### Eficiência de produção
```dax
Eficiência de Produção =
DIVIDE(
    AVERAGE(SensorData[consumo_kwh]),
    AVERAGE(SensorData[producao_hora]),
    0
)
```

## Visual e estilo
- Background escuro com gradientes azul/roxo
- Cards com bordas arredondadas e fundo levemente translúcido
- Texto grande para KPI principais
- Barras e linhas com cores vibrantes: azul, verde, laranja e roxo
- Ícones simples para cada métrica chave
- Uso de filtros no topo ou barra lateral similar aos exemplos

## Fontes e temas
- Tema de cores: azul escuro, roxo, verde neon, branco
- Fonte: Segoe UI ou Calibri
- Use cores de destaque para valores positivos e alertas vermelhos para anomalias

## Fontes de dados via API
Para atualizar o relatório automaticamente, use:
- `GET http://127.0.0.1:8000/api/overview`
- `GET http://127.0.0.1:8000/api/timeline`
- `GET http://127.0.0.1:8000/api/machines`
- `GET http://127.0.0.1:8000/api/analytics?machine={machine}`
- `GET http://127.0.0.1:8000/api/predictions`
- `GET http://127.0.0.1:8000/api/export/sensor-data`
- `GET http://127.0.0.1:8000/api/export/predictions`

## Próximo passo
1. Carregar dados no Power BI Desktop via JSON/CSV
2. Criar tabela de datas e relacionamentos
3. Adicionar cartões KPI e gráficos de tendência
4. Ajustar tema escuro e layout conforme os exemplos
