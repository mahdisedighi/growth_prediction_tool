import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const submitPrediction = async (data: Record<string, number>, token: string) => {
  return await axios.post(`${API_URL}submit-prediction/`, data, {
    headers: { Authorization: `Bearer ${token}` },
  });
};

export const getPredictionHistory = async (token: string) => {
  return await axios.get(`${API_URL}prediction-history/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};