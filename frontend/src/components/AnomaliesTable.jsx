function AnomaliesTable({ data }) {
  return (
    <div className="chart-container">
      <h3 className="text-lg font-semibold mb-4 text-white">Anomalias Detectadas</h3>
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-dark-border">
              <th className="text-left py-3 px-4 text-gray-400">Série</th>
              <th className="text-left py-3 px-4 text-gray-400">Ano</th>
              <th className="text-left py-3 px-4 text-gray-400">Valor Observado</th>
              <th className="text-left py-3 px-4 text-gray-400">Valor Esperado</th>
              <th className="text-left py-3 px-4 text-gray-400">Tipo</th>
              <th className="text-left py-3 px-4 text-gray-400">Severidade</th>
              <th className="text-left py-3 px-4 text-gray-400">Data</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index} className="border-b border-dark-border hover:bg-dark-bg">
                <td className="py-3 px-4">{item.series_key}</td>
                <td className="py-3 px-4">{item.anomaly_year || '-'}</td>
                <td className="py-3 px-4">{item.observed_value ?? '-'}</td>
                <td className="py-3 px-4">{item.expected_value ?? '-'}</td>
                <td className="py-3 px-4">{item.anomaly_type || '-'}</td>
                <td className="py-3 px-4">{item.severity || 'N/A'}</td>
                <td className="py-3 px-4">
                  {item.anomaly_date ? new Date(item.anomaly_date).toLocaleDateString('pt-BR') : '-'}
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
