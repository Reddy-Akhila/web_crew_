import React, { useState } from 'react';
import './App.css';
import AuditForm from './components/AuditForm';
import AuditResults from './components/AuditResults';
import AuditHistory from './components/AuditHistory';
import Dashboard from './components/Dashboard';

function App() {
  const [currentView, setCurrentView] = useState('dashboard');
  const [lastAudit, setLastAudit] = useState(null);
  const [auditHistory, setAuditHistory] = useState([]);

  const handleAuditComplete = (auditData) => {
    setLastAudit(auditData);
    setAuditHistory([auditData, ...auditHistory]);
    setCurrentView('results');
  };

  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>🔍 SEO Auditor Pro</h1>
        <p>Autonomous On-Page & Technical SEO Auditing</p>
      </header>

      <nav className="app-nav">
        <button 
          className={currentView === 'dashboard' ? 'active' : ''} 
          onClick={() => handleViewChange('dashboard')}
        >
          Dashboard
        </button>
        <button 
          className={currentView === 'audit' ? 'active' : ''} 
          onClick={() => handleViewChange('audit')}
        >
          New Audit
        </button>
        <button 
          className={currentView === 'history' ? 'active' : ''} 
          onClick={() => handleViewChange('history')}
        >
          Audit History
        </button>
      </nav>

      <main className="app-main">
        {currentView === 'dashboard' && <Dashboard latestAudit={lastAudit} />}
        {currentView === 'audit' && <AuditForm onComplete={handleAuditComplete} />}
        {currentView === 'results' && lastAudit && <AuditResults audit={lastAudit} />}
        {currentView === 'history' && <AuditHistory audits={auditHistory} />}
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 SEO Auditor Pro | Technical SEO Analysis Engine</p>
      </footer>
    </div>
  );
}

export default App;
