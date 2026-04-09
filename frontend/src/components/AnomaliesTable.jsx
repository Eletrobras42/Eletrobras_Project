function AnomaliesTable({ data }) {
  return (
    <div className="chart-container">
      <h3 className="text-lg font-semibold mb-4 text-white">Anomalias Detectadas</h3>
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-dark-border">
              <th className="text-left py-3 px-4 text-gray-400">Máquina</th>
              <th className="text-left py-3 px-4 text-gray-400">Tempo</th>
              <th className="text-left py-3 px-4 text-gray-400">Consumo Estimado</th>
              <th className="text-left py-3 px-4 text-gray-400">Erro %</th>
              <th className="text-left py-3 px-4 text-gray-400">Fora Tolerância</th>
              <th className="text-left py-3 px-4 text-gray-400">Anomalia</th>
              <th className="text-left py-3 px-4 text-gray-400">Data</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index} className="border-b border-dark-border hover:bg-dark-bg">
                <td className="py-3 px-4">{item.machine_name}</td>
                <td className="py-3 px-4">{item.timestamp_min} min</td>
                <td className="py-3 px-4">{item.predicted_consumo_kwh?.toFixed(2)} kWh</td>
                <td className="py-3 px-4">{item.erro_percentual?.toFixed(2)}%</td>
                <td className="py-3 px-4">
                  <span className={`px-2 py-1 rounded text-xs ${
                    item.fora_tolerancia ? 'bg-accent-red text-white' : 'bg-accent-green text-white'
                  }`}>
                    {item.fora_tolerancia ? 'Sim' : 'Não'}
                  </span>
                </td>
                <td className="py-3 px-4">
                  <span className={`px-2 py-1 rounded text-xs ${
                    item.anomalia ? 'bg-accent-orange text-white' : 'bg-accent-green text-white'
                  }`}>
                    {item.anomalia ? 'Sim' : 'Não'}
                  </span>
                </td>
                <td className="py-3 px-4">
                  {new Date(item.created_at).toLocaleDateString('pt-BR')}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AnomaliesTable;