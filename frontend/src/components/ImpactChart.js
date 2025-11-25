import React from 'react';
import './ImpactChart.css';

function ImpactChart({ impact = {} }) {
  const currentScore = impact.current_score || 0;
  const estimatedScore = impact.estimated_score_after_fixes || 0;
  const scoreImprovement = impact.score_improvement || 0;

  return (
    <div className="impact-chart-section">
      <h3>Simulated Impact</h3>

      <div className="impact-metrics">
        <div className="metric-card">
          <div className="metric-label">Current Score</div>
          <div className="metric-value">{currentScore}</div>
          <div className="metric-bar">
            <div className="metric-fill" style={{ width: `${currentScore}%` }}></div>
          </div>
        </div>

        <div className="metric-card highlight">
          <div className="metric-label">Estimated Score</div>
          <div className="metric-value">{estimatedScore}</div>
          <div className="metric-bar">
            <div className="metric-fill" style={{ width: `${estimatedScore}%`, backgroundColor: '#4caf50' }}></div>
          </div>
        </div>

        <div className="metric-card improvement">
          <div className="metric-label">Score Improvement</div>
          <div className="metric-value">+{scoreImprovement}</div>
          <div className="improvement-percentage">{(scoreImprovement / 100 * 100).toFixed(1)}% increase</div>
        </div>
      </div>

      <div className="impact-projections">
        <div className="projection-item">
          <h4>📈 Traffic Improvement</h4>
          <p className="projection-value">{impact.estimated_traffic_improvement_percent}%</p>
          <p className="projection-desc">Estimated increase in organic traffic</p>
        </div>

        <div className="projection-item">
          <h4>🎯 Keyword Rankings</h4>
          <p className="projection-value">{impact.estimated_keyword_ranking_improvement}</p>
          <p className="projection-desc">Average position improvement</p>
        </div>

        <div className="projection-item">
          <h4>⏱️ Time to Results</h4>
          <p className="projection-value">{impact.timeframe_to_see_results_days} days</p>
          <p className="projection-desc">Expected time frame for changes to take effect</p>
        </div>

        <div className="projection-item">
          <h4>📊 Confidence Level</h4>
          <p className="projection-value">{impact.confidence_level}</p>
          <p className="projection-desc">Based on number of critical issues</p>
        </div>
      </div>
    </div>
  );
}

export default ImpactChart;
