import React from 'react';
import './ScoreCard.css';

function ScoreCard({ score, label, icon, isNegative = false }) {
  const getScoreColor = (value) => {
    if (isNegative) {
      return value === 0 ? '#4caf50' : '#ff6b6b';
    }
    if (value >= 80) return '#4caf50';
    if (value >= 60) return '#ffc107';
    return '#ff6b6b';
  };

  return (
    <div className="score-card">
      <div className="score-icon">{icon}</div>
      <div className="score-value" style={{ color: getScoreColor(score) }}>
        {typeof score === 'number' && !isNegative ? score.toFixed(1) : score}
      </div>
      <div className="score-label">{label}</div>
    </div>
  );
}

export default ScoreCard;
