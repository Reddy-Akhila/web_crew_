import React from 'react';
import './AuditResults.css';
import ScoreCard from './ScoreCard';
import IssuesList from './IssuesList';
import RecommendationsList from './RecommendationsList';
import ImpactChart from './ImpactChart';

function AuditResults({ audit }) {
  return (
    <div className="audit-results">
      <div className="results-header">
        <h2>Audit Results for {audit.url}</h2>
        <p className="timestamp">{new Date(audit.timestamp).toLocaleString()}</p>
      </div>

      <div className="results-grid">
        <ScoreCard
          score={audit.seo_score}
          label="Overall SEO Score"
          icon="🎯"
        />
        <ScoreCard
          score={audit.crawl_summary.total_pages}
          label="Pages Audited"
          icon="📄"
        />
        <ScoreCard
          score={audit.crawl_summary.broken_links}
          label="Broken Links Found"
          icon="🔗"
          isNegative={true}
        />
        <ScoreCard
          score={audit.crawl_summary.crawl_time.toFixed(2)}
          label="Crawl Time (seconds)"
          icon="⏱️"
        />
      </div>

      <div className="results-content">
        <div className="results-section">
          <IssuesList issues={audit.issues} />
        </div>

        <div className="results-section">
          <ImpactChart impact={audit.simulated_impact} />
        </div>

        <div className="results-section">
          <RecommendationsList recommendations={audit.recommendations} />
        </div>
      </div>

      <div className="results-footer">
        <button onClick={() => window.print()} className="export-button">
          📥 Export as PDF
        </button>
      </div>
    </div>
  );
}

export default AuditResults;
