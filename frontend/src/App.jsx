import { useState } from 'react';
import { BarChart3, Zap } from 'lucide-react';
import PredictionForm from './components/PredictionForm.jsx';
import StatusCard from './components/StatusCard.jsx';
import Dashboard from './pages/Dashboard.jsx';

function App() {
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState('');
  const [currentView, setCurrentView] = useState('predict'); // 'predict' or 'dashboard'

  if (currentView === 'dashboard') {
    return <Dashboard />;
  }

  return (
    <div className="min-h-screen bg-gradient-dark">
      <div className="container mx-auto px-6 py-8">
        {/* Navigation */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-white mb-2">
              Eletrobras Predictive Monitoring
            </h1>
            <p className="text-gray-400">
              Sistema de predição e análise energética
            </p>
          </div>

          <button
            onClick={() => setCurrentView('dashboard')}
            className="flex items-center px-6 py-3 bg-accent-blue hover:bg-blue-600 text-white rounded-lg transition-colors"
          >
            <BarChart3 size={18} className="mr-2" />
            Dashboard BI
          </button>
        </div>

        {/* Prediction Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-6">
            <div className="card">
              <div className="flex items-center mb-6">
                <Zap className="text-accent-blue mr-3" size={24} />
                <h2 className="text-xl font-semibold text-white">Solicitar Previsão</h2>
              </div>
              <PredictionForm onResult={setPrediction} onError={setError} />
            </div>
          </div>

          <div className="space-y-6">
            {error && (
              <div className="card border-accent-red">
                <p className="text-accent-red">{error}</p>
              </div>
            )}

            {prediction && (
              <div className="card">
                <StatusCard result={prediction} />
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
