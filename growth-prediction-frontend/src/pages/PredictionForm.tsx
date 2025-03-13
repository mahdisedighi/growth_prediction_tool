import React, { useState } from 'react';
import { submitPrediction } from '../services/predictionService';
import '../styles.css';

const PredictionForm: React.FC = () => {
  const [formData, setFormData] = useState({
    revenue_growth: 0,
    market_share: 0,
    digital_engagement_score: 0,
    consumer_loyalty_score: 0,
    marketing_budget_allocation: 0,
    sustainability_index: 0,
    e_commerce_market_share: 0,
    physical_retail_presence: 0,
    competition_level: 0,
  });

  // Updated result state to include insights as an array of strings
  const [result, setResult] = useState<{ success_score: number; risk_level: string; insights: string[] } | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      if (!token) throw new Error('No token found');
      const response = await submitPrediction(formData, token);
      setResult(response.data);
    } catch (error) {
      alert('Submission failed');
    }
  };

  return (
    <div className="form-container">
      <h2>Growth Prediction Form</h2>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-section">
          <h3>Financial Data</h3>
          <input name="revenue_growth" onChange={handleChange} placeholder="Revenue Growth" type="number" required />
          <input name="market_share" onChange={handleChange} placeholder="Market Share" type="number" required />
        </div>
        <div className="form-section">
          <h3>Engagement & Loyalty</h3>
          <input name="digital_engagement_score" onChange={handleChange} placeholder="Digital Engagement Score" type="number" required />
          <input name="consumer_loyalty_score" onChange={handleChange} placeholder="Consumer Loyalty Score" type="number" required />
        </div>
        <div className="form-section">
          <h3>Marketing & Sustainability</h3>
          <input name="marketing_budget_allocation" onChange={handleChange} placeholder="Marketing Budget Allocation" type="number" required />
          <input name="sustainability_index" onChange={handleChange} placeholder="Sustainability Index" type="number" required />
        </div>
        <div className="form-section">
          <h3>Market Presence</h3>
          <input name="e_commerce_market_share" onChange={handleChange} placeholder="E-commerce Market Share" type="number" required />
          <input name="physical_retail_presence" onChange={handleChange} placeholder="Physical Retail Presence" type="number" required />
        </div>
        <div className="form-section">
          <h3>Competition</h3>
          <input name="competition_level" onChange={handleChange} placeholder="Competition Level" type="number" required />
        </div>
        <button type="submit">Submit</button>
      </form>

      {result && (
        <div className="result-container">
          <h3>Prediction Result</h3>
          <p><strong>Success Score:</strong> {result.success_score}</p>
          <p><strong>Risk Level:</strong> {result.risk_level}</p>
          {/* Display market insights if available */}
          {result.insights && result.insights.length > 0 && (
            <div>
              <h4>Market Insights:</h4>
              <ul>
                {result.insights.map((insight, index) => (
                  <li key={index}>{insight}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default PredictionForm;