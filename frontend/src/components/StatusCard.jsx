import { CheckCircle, XCircle, AlertTriangle, Clock } from 'lucide-react';

function StatusCard({ result }) {
  const getStatusIcon = (anomalia, foraTolerancia) => {
    if (anomalia) return <AlertTriangle className="text-accent-orange" size={20} />;
    if (foraTolerancia) return <XCircle className="text-accent-red" size={20} />;
    return <CheckCircle className="text-accent-green" size={20} />;
  };

  const getStatusText = (anomalia, foraTolerancia) => {
    if (anomalia) return "Anomalia detectada";
    if (foraTolerancia) return "Fora da tolerância";
    return "Dentro da normalidade";
  };

  const getStatusColor = (anomalia, foraTolerancia) => {
    if (anomalia) return "border-accent-orange";
    if (foraTolerancia) return "border-accent-red";
    return "border-accent-green";
  };

  return (
    <div className={`card ${getStatusColor(result.anomalia, result.fora_tolerancia)}`}>
      <div className="flex items-center mb-6">
        {getStatusIcon(result.anomalia, result.fora_tolerancia)}
        <h2 className="text-xl font-semibold text-white ml-3">Resultado da Previsão</h2>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Máquina</div>
          <div className="text-lg font-semibold text-white">{result.machine}</div>
        </div>

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Tempo Informado</div>
          <div className="text-lg font-semibold text-white">{result.time} min</div>
        </div>

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Consumo Estimado</div>
          <div className="text-lg font-semibold text-accent-blue">{result.consumo_estimado.toFixed(2)} kWh</div>
        </div>

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Erro Percentual</div>
          <div className="text-lg font-semibold text-accent-purple">{result.erro_percentual}%</div>
        </div>

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Fora da Tolerância</div>
          <div className={`text-lg font-semibold ${result.fora_tolerancia ? 'text-accent-red' : 'text-accent-green'}`}>
            {result.fora_tolerancia ? 'Sim' : 'Não'}
          </div>
        </div>

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Anomalia</div>
          <div className={`text-lg font-semibold ${result.anomalia ? 'text-accent-orange' : 'text-accent-green'}`}>
            {result.anomalia ? 'Sim' : 'Não'}
          </div>
        </div>

        {result.worker_activity_min && (
          <div className="bg-dark-bg p-4 rounded-lg">
            <div className="text-sm text-gray-400 mb-1">Tempo de Atividade</div>
            <div className="text-lg font-semibold text-accent-green">{result.worker_activity_min} min</div>
          </div>
        )}

        <div className="bg-dark-bg p-4 rounded-lg">
          <div className="text-sm text-gray-400 mb-1">Status</div>
          <div className="text-lg font-semibold text-white">{getStatusText(result.anomalia, result.fora_tolerancia)}</div>
        </div>
      </div>

      <div className="mt-6 pt-4 border-t border-dark-border">
        <div className="flex items-center text-sm text-gray-400">
          <Clock size={16} className="mr-2" />
          Baseado em {result.history_count} registros históricos
        </div>
      </div>
    </div>
  );
}

export default StatusCard;
