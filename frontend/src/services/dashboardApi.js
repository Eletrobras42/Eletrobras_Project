import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 10000,
});

export async function getDashboardOverview() {
  const response = await api.get('/overview');
  return response.data;
}

export async function getTimelineData() {
  const response = await api.get('/timeline');
  return response.data;
}

export async function getMachineAnalytics(machine) {
  const response = await api.get(`/analytics?machine=${machine}`);
  return response.data;
}

export async function getPredictions(machine = null) {
  const url = machine ? `/predictions?machine=${machine}` : '/predictions';
  const response = await api.get(url);
  return response.data;
}

export async function getMachines() {
  const response = await api.get('/machines');
  return response.data;
}

export default api;