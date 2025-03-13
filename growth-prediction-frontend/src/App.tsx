import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import PredictionForm from './pages/PredictionForm';
import PredictionHistory from './pages/PredictionHistory';
import './styles.css';

function App() {
  const token = localStorage.getItem('token');

  const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
    return token ? children : <Navigate to="/login" />;
  };

  return (
    <Router>
      <div className="container">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/predict" element={<ProtectedRoute><PredictionForm /></ProtectedRoute>} />
          <Route path="/history" element={<ProtectedRoute><PredictionHistory /></ProtectedRoute>} />
          <Route path="/" element={<HomePage token={token} />} />
        </Routes>
      </div>
    </Router>
  );
}

const HomePage = ({ token }: { token: string | null }) => {
  const navigate = useNavigate();

  return (
    <div className="home-page">
      <h2>Welcome to the Growth Prediction Tool</h2>
      {token ? (
        <>
          <div className="welcome-box">
            <p>Welcome, <strong>{localStorage.getItem('username') || 'User'}</strong>! Track your growth.</p>
          </div>
          <div className="navbar">
            <button onClick={() => navigate('/predict')}>Prediction Form</button>
            <button onClick={() => navigate('/history')}>Prediction History</button>
            <button onClick={() => {
              localStorage.removeItem('token');
              localStorage.removeItem('username');
              navigate('/login');
            }}>
              Logout
            </button>
          </div>
        </>
      ) : (
        <>
          <p className="description">Your one-stop solution for predicting your clothing brand's growth in the Middle East.</p>
          <div className="button-group">
            <button onClick={() => navigate('/login')}>Login</button>
            <button onClick={() => navigate('/register')}>Register</button>
          </div>
        </>
      )}
    </div>
  );
};

export default App;