import React from 'react';
import './Dashboard.css';

function Dashboard({ latestAudit = null }) {
  return (
    <div className="dashboard">
      <div className="dashboard-grid">
        <div className="dashboard-card feature-card">
          <div className="card-icon">🕷️</div>
          <h3>Web Crawling Engine</h3>
          <p>Intelligent crawling with configurable depth levels (1-4), extracts meta data, checks internal/external links, and measures page load times.</p>
          <ul className="features-list">
            <li>Multi-level crawling</li>
            <li>Link validation</li>
            <li>Performance metrics</li>
          </ul>
        </div>

        <div className="dashboard-card feature-card">
          <div className="card-icon">🤖</div>
          <h3>AI-Based Scoring</h3>
          <p>Comprehensive SEO analysis identifying broken links, mobile-friendliness issues, schema validation, page speed, and duplicate content detection.</p>
          <ul className="features-list">
            <li>Broken link detection</li>
            <li>Mobile check</li>
            <li>Schema validation</li>
          </ul>
        </div>

        <div className="dashboard-card feature-card">
          <div className="card-icon">🔧</div>
          <h3>Auto Recommendations</h3>
          <p>Prioritized improvement suggestions with difficulty ratings, time estimates, code snippets, and simulated ranking impact calculations.</p>
          <ul className="features-list">
            <li>Priority ranking</li>
            <li>Impact simulation</li>
            <li>Code templates</li>
          </ul>
        </div>

        <div className="dashboard-card feature-card">
          <div className="card-icon">📊</div>
          <h3>Visual Dashboard</h3>
          <p>Interactive charts and reports with overall SEO scores, category breakdown, before/after comparisons, and downloadable PDF reports.</p>
          <ul className="features-list">
            <li>Real-time charts</li>
            <li>Score breakdown</li>
            <li>PDF reports</li>
          </ul>
        </div>
      </div>

      {latestAudit && (
        <div className="latest-audit-card">
          <h3>Latest Audit Results</h3>
          <div className="audit-summary">
            <div className="summary-item">
              <span className="label">URL:</span>
              <span className="value">{latestAudit.url}</span>
            </div>
            <div className="summary-item">
              <span className="label">SEO Score:</span>
              <span className="value score">{latestAudit.seo_score}</span>
            </div>
            <div className="summary-item">
              <span className="label">Pages Audited:</span>
              <span className="value">{latestAudit.crawl_summary.total_pages}</span>
            </div>
            <div className="summary-item">
              <span className="label">Issues Found:</span>
              <span className="value">{latestAudit.issues.length}</span>
            </div>
          </div>
        </div>
      )}

      <div className="getting-started">
        <h3>Getting Started</h3>
        <div className="steps">
          <div className="step">
            <div className="step-number">1</div>
            <div className="step-content">
              <h4>Enter Website URL</h4>
              <p>Navigate to "New Audit" and enter your website URL</p>
            </div>
          </div>
          <div className="step">
            <div className="step-number">2</div>
            <div className="step-content">
              <h4>Select Crawl Depth</h4>
              <p>Choose how deep you want the crawler to go (1-4 levels)</p>
            </div>
          </div>
          <div className="step">
            <div className="step-number">3</div>
            <div className="step-content">
              <h4>Run Audit</h4>
              <p>The system will analyze your site and generate recommendations</p>
            </div>
          </div>
          <div className="step">
            <div className="step-number">4</div>
            <div className="step-content">
              <h4>Review & Implement</h4>
              <p>View detailed reports and optionally auto-implement fixes</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
