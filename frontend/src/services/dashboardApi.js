import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 10000,
});

export async function getDashboardOverview() {
  const response = await api.get('/dashboard/kpis');
  return response.data;
}

export async function getDashboardTrends() {
  const response = await api.get('/dashboard/trends');
  return response.data;
}

export async function getDashboardAnomalies() {
  const response = await api.get('/dashboard/anomalies');
  return response.data;
}

export async function getSources() {
  const response = await api.get('/sources');
  return response.data;
}

export default api;