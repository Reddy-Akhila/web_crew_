import React from 'react';
import './RecommendationsList.css';

function RecommendationsList({ recommendations = [] }) {
  const difficultyEmoji = {
    'Easy': '✅',
    'Medium': '⚠️',
    'Hard': '🔴'
  };

  return (
    <div className="recommendations-section">
      <div className="section-header">
        <h3>Improvement Recommendations</h3>
        <span className="rec-count">{recommendations.length} recommendations</span>
      </div>

      {recommendations.length === 0 ? (
        <div className="empty-state">
          <p>No recommendations available</p>
        </div>
      ) : (
        <div className="recommendations-list">
          {recommendations.map((rec, index) => (
            <div key={rec.id} className="recommendation-card">
              <div className="rec-header">
                <div className="rec-title">
                  <span className="rec-priority">Priority #{rec.fix_priority}</span>
                  <h4>{rec.title}</h4>
                </div>
                <div className="rec-status" data-status={rec.status}>
                  {rec.status === 'fixed' ? '✓ Fixed' : '⧖ Pending'}
                </div>
              </div>

              <p className="rec-description">{rec.description}</p>

              <div className="rec-details">
                <div className="detail-item">
                  <strong>Affected Pages:</strong> {rec.affected_pages}
                </div>
                <div className="detail-item">
                  <strong>Difficulty:</strong> {difficultyEmoji[rec.implementation_difficulty]} {rec.implementation_difficulty}
                </div>
                <div className="detail-item">
                  <strong>Time to Fix:</strong> ~{rec.time_to_fix_minutes} minutes
                </div>
              </div>

              <div className="rec-impact">
                <div className="impact-item">
                  <span className="impact-label">Ranking Impact:</span>
                  <span className="impact-value">{rec.estimated_ranking_impact}</span>
                </div>
                <div className="impact-item">
                  <span className="impact-label">Traffic Impact:</span>
                  <span className="impact-value">{rec.estimated_traffic_impact}</span>
                </div>
              </div>

              <div className="code-snippet">
                <strong>Code Snippet:</strong>
                <pre><code>{rec.code_snippet}</code></pre>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default RecommendationsList;
