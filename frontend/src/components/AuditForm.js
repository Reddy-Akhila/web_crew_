import React, { useState } from 'react';
import axios from 'axios';
import './AuditForm.css';

function AuditForm({ onComplete }) {
  const [url, setUrl] = useState('');
  const [depth, setDepth] = useState(2);
  const [autoFix, setAutoFix] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await axios.post('/api/audit', {
        url,
        depth: parseInt(depth),
        auto_fix: autoFix
      });

      onComplete(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Error running audit. Please check the URL.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="audit-form-container">
      <div className="audit-form-card">
        <h2>Start New SEO Audit</h2>
        <p className="form-description">
          Enter a website URL to perform a comprehensive technical SEO audit
        </p>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="url">Website URL *</label>
            <input
              type="url"
              id="url"
              placeholder="https://example.com"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
              disabled={loading}
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="depth">Crawl Depth</label>
              <select
                id="depth"
                value={depth}
                onChange={(e) => setDepth(e.target.value)}
                disabled={loading}
              >
                <option value="1">1 Level (Homepage only)</option>
                <option value="2">2 Levels (Default)</option>
                <option value="3">3 Levels (Comprehensive)</option>
                <option value="4">4 Levels (Deep Crawl)</option>
              </select>
            </div>

            <div className="form-group checkbox">
              <label htmlFor="auto-fix">
                <input
                  type="checkbox"
                  id="auto-fix"
                  checked={autoFix}
                  onChange={(e) => setAutoFix(e.target.checked)}
                  disabled={loading}
                />
                Auto-implement fixes
              </label>
            </div>
          </div>

          {error && <div className="error-message">{error}</div>}

          <button type="submit" disabled={loading} className="submit-button">
            {loading ? (
              <>
                <span className="spinner"></span> Auditing...
              </>
            ) : (
              'Start Audit'
            )}
          </button>
        </form>

        <div className="info-box">
          <h3>What This Audit Checks:</h3>
          <ul>
            <li>✅ Page titles and meta descriptions</li>
            <li>✅ Heading structure (H1, H2, etc.)</li>
            <li>✅ Image alt text</li>
            <li>✅ Canonical tags and robots directives</li>
            <li>✅ Mobile-friendliness</li>
            <li>✅ Broken links</li>
            <li>✅ Schema markup</li>
            <li>✅ Page load performance</li>
            <li>✅ Content length and quality</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default AuditForm;
