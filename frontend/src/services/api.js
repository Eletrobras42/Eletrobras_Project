import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 8000,
});

export async function predict(payload) {
  const response = await api.post('/predict', payload);
  return response.data;
}

export default api;
