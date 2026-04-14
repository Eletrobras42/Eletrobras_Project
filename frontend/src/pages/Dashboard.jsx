import { useState, useEffect } from 'react';
import { BarChart3, TrendingUp, AlertTriangle, Activity } from 'lucide-react';
import KPICard from '../components/KPICard.jsx';
import TimelineChart from '../components/TimelineChart.jsx';
import AnomaliesTable from '../components/AnomaliesTable.jsx';
import { getDashboardOverview, getDashboardTrends, getDashboardAnomalies } from '../services/dashboardApi.js';

function Dashboard() {
  const [overview, setOverview] = useState(null);
  const [trends, setTrends] = useState([]);
  const [anomalies, setAnomalies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    loadDashboardData();
  }, []);

  async function loadDashboardData() {
    try {
      setLoading(true);
      const [overviewData, trendsData, anomaliesData] = await Promise.all([
        getDashboardOverview(),
        getDashboardTrends(),
        getDashboardAnomalies(),
      ]);

      setOverview(overviewData);
      setTrends(trendsData);
      setAnomalies(anomaliesData);
    } catch (err) {
      setError('Erro ao carregar dados do dashboard');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-dark-bg flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-accent-blue mx-auto mb-4"></div>
          <p className="text-gray-400">Carregando dashboard...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-dark-bg flex items-center justify-center">
        <div className="text-center">
          <AlertTriangle size={48} className="text-accent-red mx-auto mb-4" />
          <p className="text-accent-red">{error}</p>
          <button
            onClick={loadDashboardData}
            className="mt-4 px-6 py-2 bg-accent-blue rounded-lg hover:bg-blue-600 transition-colors"
          >
            Tentar Novamente
          </button>
        </div>
      </div>
    );
  }

  // Preparar dados para os gráficos
  const chartData = trends.reduce((acc, item) => {
    const year = item.observation_year;
    const existing = acc.find((row) => row.year === year);

    if (existing) {
      existing[item.series_key] = item.numeric_value;
      return acc;
    }

    return [...acc, { year, [item.series_key]: item.numeric_value }];
  }, []);

  const anomaliesData = anomalies.slice(0, 10);

  const tabs = [
    { id: 'overview', label: 'Visão Executiva', icon: BarChart3 },
    { id: 'anomalies', label: 'Anomalias', icon: AlertTriangle },
    { id: 'timeline', label: 'Tendências', icon: TrendingUp },
  ];

  return (
    <div className="min-h-screen bg-gradient-dark">
      <div className="container mx-auto px-6 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-white mb-2">
            Eletrobras Predictive Monitoring
          </h1>
          <p className="text-gray-400">
            Dashboard de análise energética e detecção de anomalias
          </p>
        </div>

        {/* Navigation Tabs */}
        <div className="flex space-x-1 mb-8 bg-dark-card p-1 rounded-lg">
          {tabs.map(tab => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center px-6 py-3 rounded-md transition-all ${
                  activeTab === tab.id
                    ? 'bg-accent-blue text-white shadow-lg'
                    : 'text-gray-400 hover:text-white hover:bg-dark-bg'
                }`}
              >
                <Icon size={18} className="mr-2" />
                {tab.label}
              </button>
            );
          })}
        </div>

        {/* Content */}
        {activeTab === 'overview' && overview && (
          <div className="space-y-8">
            {/* KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <KPICard
                title="Documentos Catalogados"
                value={overview.documents_cataloged}
                icon={Activity}
                color="blue"
              />
              <KPICard
                title="Indicadores Extraídos"
                value={overview.indicators_extracted}
                icon={BarChart3}
                color="purple"
              />
              <KPICard
                title="Séries Consolidadas"
                value={overview.series_consolidated}
                icon={TrendingUp}
                color="green"
              />
              <KPICard
                title="Anomalias Detectadas"
                value={overview.anomalies_detected}
                icon={AlertTriangle}
                color="orange"
              />
            </div>

            {/* Charts */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <TimelineChart
                data={chartData}
                title="Tendência de Indicadores"
                dataKey={Object.keys(chartData[0] || {}).find((key) => key !== 'year') || 'value'}
                xDataKey="year"
                color="#3b82f6"
              />
              <div className="chart-container">
                <h3 className="text-lg font-semibold mb-4 text-white">Resumo Analítico</h3>
                <p className="text-gray-300 leading-relaxed">
                  Este dashboard consolida o catálogo de documentos, indicadores e séries históricas
                  alinhados ao modelo de governança de dados da Eletrobras.
                </p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'anomalies' && (
          <div className="space-y-8">
            {/* Anomalies KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <KPICard
                title="Execuções de Ingestão"
                value={overview?.ingestion_runs || 0}
                icon={BarChart3}
                color="blue"
              />
              <KPICard
                title="Anomalias Detectadas"
                value={overview?.anomalies_detected || 0}
                icon={AlertTriangle}
                color="red"
              />
              <KPICard
                title="Séries Consolidadas"
                value={overview?.series_consolidated || 0}
                icon={TrendingUp}
                color="orange"
              />
            </div>

            {/* Anomalies Table */}
            <AnomaliesTable data={anomaliesData} />
          </div>
        )}

        {activeTab === 'timeline' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <TimelineChart
                data={chartData}
                title="Tendência de Série Histórica"
                dataKey={Object.keys(chartData[0] || {}).find((key) => key !== 'year') || 'value'}
                xDataKey="year"
                color="#10b981"
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;