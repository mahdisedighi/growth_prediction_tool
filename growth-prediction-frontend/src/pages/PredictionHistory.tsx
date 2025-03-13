import React, { useState, useEffect } from 'react';
import { getPredictionHistory } from '../services/predictionService';
import '../styles.css';

interface Prediction {
  _id: string;
  success_score: number;
  revenue_growth: number;
  market_share: number;
  digital_engagement_score: number;
  consumer_loyalty_score: number;
  marketing_budget_allocation: number;
  sustainability_index: number;
  e_commerce_market_share: number;
  physical_retail_presence: number;
  competition_level: number;
  created_at: string;
  risk_level?: string;
  insights?: string[]; // Added optional insights field
}

const PredictionHistory: React.FC = () => {
  const [predictions, setPredictions] = useState<Prediction[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [expanded, setExpanded] = useState<string | null>(null);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          setError('Please log in to view your prediction history.');
          setLoading(false);
          return;
        }
        const response = await getPredictionHistory(token);
        setPredictions(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch prediction history.');
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  const toggleExpand = (id: string) => {
    setExpanded(expanded === id ? null : id);
  };

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="prediction-history">
      <h2>Prediction History</h2>
      {predictions.length === 0 ? (
        <p>No predictions found.</p>
      ) : (
        predictions.map((pred) => (
          <div key={pred._id} className="prediction-box">
            <div className="prediction-summary" onClick={() => toggleExpand(pred._id)}>
              <p><strong>Success Score:</strong> {pred.success_score}</p>
              <p><strong>Date:</strong> {new Date(pred.created_at).toLocaleString()}</p>
              <button>{expanded === pred._id ? 'Collapse' : 'Expand'}</button>
            </div>
            {expanded === pred._id && (
              <div className="prediction-details">
                <p><strong>Risk Level:</strong> {pred.risk_level || 'N/A'}</p>
                <p><strong>Revenue Growth:</strong> {pred.revenue_growth}</p>
                <p><strong>Market Share:</strong> {pred.market_share}</p>
                <p><strong>Digital Engagement:</strong> {pred.digital_engagement_score}</p>
                <p><strong>Consumer Loyalty:</strong> {pred.consumer_loyalty_score}</p>
                <p><strong>Marketing Budget:</strong> {pred.marketing_budget_allocation}</p>
                <p><strong>Sustainability Index:</strong> {pred.sustainability_index}</p>
                <p><strong>E-commerce Share:</strong> {pred.e_commerce_market_share}</p>
                <p><strong>Retail Presence:</strong> {pred.physical_retail_presence}</p>
                <p><strong>Competition Level:</strong> {pred.competition_level}</p>
                {/* Display market insights if available */}
                {pred.insights && pred.insights.length > 0 && (
                  <div>
                    <h4>Market Insights:</h4>
                    <ul>
                      {pred.insights.map((insight, index) => (
                        <li key={index}>{insight}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}
          </div>
        ))
      )}
    </div>
  );
};

export default PredictionHistory;