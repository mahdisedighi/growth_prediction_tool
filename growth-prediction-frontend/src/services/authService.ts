import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const register = async (username: string, password: string) => {
  return await axios.post(`${API_URL}register/`, { username, password });
};

export const login = async (username: string, password: string) => {
  return await axios.post(`${API_URL}token/`, { username, password });
};