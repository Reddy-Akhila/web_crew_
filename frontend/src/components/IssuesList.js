import React, { useState } from 'react';
import './IssuesList.css';

function IssuesList({ issues = [] }) {
  const [filter, setFilter] = useState('all');

  const severityOrder = { critical: 0, high: 1, medium: 2, low: 3 };
  const filteredIssues = filter === 'all' 
    ? issues 
    : issues.filter(issue => issue.severity === filter);

  filteredIssues.sort((a, b) => severityOrder[a.severity] - severityOrder[b.severity]);

  const severityColors = {
    critical: '#ff6b6b',
    high: '#ff9800',
    medium: '#ffc107',
    low: '#2196f3'
  };

  return (
    <div className="issues-section">
      <div className="section-header">
        <h3>Issues Found</h3>
        <div className="filter-buttons">
          <button 
            className={filter === 'all' ? 'active' : ''} 
            onClick={() => setFilter('all')}
          >
            All ({issues.length})
          </button>
          <button 
            className={filter === 'critical' ? 'active' : ''} 
            onClick={() => setFilter('critical')}
          >
            Critical ({issues.filter(i => i.severity === 'critical').length})
          </button>
          <button 
            className={filter === 'high' ? 'active' : ''} 
            onClick={() => setFilter('high')}
          >
            High ({issues.filter(i => i.severity === 'high').length})
          </button>
        </div>
      </div>

      {filteredIssues.length === 0 ? (
        <div className="empty-state">
          <p>✅ No {filter === 'all' ? 'issues' : filter + ' issues'} found!</p>
        </div>
      ) : (
        <div className="issues-list">
          {filteredIssues.map((issue, index) => (
            <div key={index} className="issue-item">
              <div className="issue-severity" style={{ backgroundColor: severityColors[issue.severity] }}>
                {issue.severity.toUpperCase()}
              </div>
              <div className="issue-content">
                <h4>{issue.title}</h4>
                <p>{issue.description}</p>
                {issue.links && (
                  <div className="issue-links">
                    <strong>Affected:</strong> {issue.links.slice(0, 2).join(', ')}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default IssuesList;
