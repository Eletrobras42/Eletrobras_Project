import { useState } from 'react';
import { Send, Loader2 } from 'lucide-react';
import { predict } from '../services/api.js';

function PredictionForm({ onResult, onError }) {
  const [machine, setMachine] = useState('Linha 1');
  const [time, setTime] = useState(75);
  const [workerActivity, setWorkerActivity] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    onError('');
    onResult(null);

    try {
      const payload = {
        machine,
        time: Number(time),
      };
      if (workerActivity) {
        payload.worker_activity_min = Number(workerActivity);
      }

      const data = await predict(payload);
      onResult(data);
    } catch (err) {
      onError(err.response?.data?.detail || 'Erro ao chamar a API de previsão. Verifique se o backend está rodando.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h2 className="text-xl font-semibold text-white mb-6">Solicitar Previsão</h2>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="machine" className="block text-sm font-medium text-gray-300 mb-2">
            Máquina
          </label>
          <select
            id="machine"
            name="machine"
            value={machine}
            onChange={(e) => setMachine(e.target.value)}
            className="w-full px-4 py-3 bg-dark-bg border border-dark-border rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-accent-blue focus:border-transparent"
            required
          >
            <option value="Linha 1">Linha 1</option>
            <option value="Linha 2">Linha 2</option>
            <option value="Linha 3">Linha 3</option>
            <option value="Linha 4">Linha 4</option>
          </select>
        </div>

        <div>
          <label htmlFor="time" className="block text-sm font-medium text-gray-300 mb-2">
            Tempo (minutos)
          </label>
          <input
            type="number"
            id="time"
            name="time"
            value={time}
            onChange={(e) => setTime(e.target.value)}
            min="0"
            className="w-full px-4 py-3 bg-dark-bg border border-dark-border rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-accent-blue focus:border-transparent"
            placeholder="Digite o tempo em minutos"
            required
          />
        </div>

        <div>
          <label htmlFor="workerActivity" className="block text-sm font-medium text-gray-300 mb-2">
            Tempo de Atividade do Colaborador (minutos)
          </label>
          <input
            type="number"
            id="workerActivity"
            name="workerActivity"
            value={workerActivity}
            onChange={(e) => setWorkerActivity(e.target.value)}
            min="0"
            className="w-full px-4 py-3 bg-dark-bg border border-dark-border rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-accent-blue focus:border-transparent"
            placeholder="Opcional"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-gradient-to-r from-accent-blue to-accent-purple hover:from-accent-blue/80 hover:to-accent-purple/80 disabled:from-gray-600 disabled:to-gray-600 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 flex items-center justify-center gap-2 disabled:cursor-not-allowed"
        >
          {loading ? (
            <>
              <Loader2 size={20} className="animate-spin" />
              Analisando...
            </>
          ) : (
            <>
              <Send size={20} />
              Enviar
            </>
          )}
        </button>
      </form>
    </div>
  );
}

export default PredictionForm;
