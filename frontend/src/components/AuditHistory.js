import React from 'react';
import './AuditHistory.css';

function AuditHistory({ audits = [] }) {
  const getScoreColor = (score) => {
    if (score >= 80) return '#4caf50';
    if (score >= 60) return '#ffc107';
    return '#ff6b6b';
  };

  return (
    <div className="audit-history-container">
      <div className="history-header">
        <h2>Audit History</h2>
        <p>Previously completed audits</p>
      </div>

      {audits.length === 0 ? (
        <div className="empty-state">
          <h3>No audits yet</h3>
          <p>Run your first audit to see it appear here</p>
        </div>
      ) : (
        <div className="history-table">
          <table>
            <thead>
              <tr>
                <th>Website</th>
                <th>Date & Time</th>
                <th>Pages Audited</th>
                <th>SEO Score</th>
                <th>Issues Found</th>
              </tr>
            </thead>
            <tbody>
              {audits.map((audit) => (
                <tr key={audit.audit_id}>
                  <td className="url-cell">{audit.url}</td>
                  <td>{new Date(audit.timestamp).toLocaleString()}</td>
                  <td className="center">{audit.pages_audited || 0}</td>
                  <td className="center">
                    <span 
                      className="score-badge" 
                      style={{ color: getScoreColor(audit.seo_score) }}
                    >
                      {audit.seo_score}
                    </span>
                  </td>
                  <td className="center">
                    <button className="issues-badge" onClick={() => alert(`${audit.issues_count || 0} issues found`)}>
                      {audit.issues_count || 0}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default AuditHistory;
