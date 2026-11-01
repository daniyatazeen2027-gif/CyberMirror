
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';
import './App.css';

import Dashboard from './pages/Dashboard';
import VehicleTwin from './pages/VehicleTwin';
import ThreatMonitoring from './pages/ThreatMonitoring';
import SecurityAlerts from './pages/SecurityAlerts';
import AttackSimulation from './pages/AttackSimulation';
import RiskAnalysis from './pages/RiskAnalysis';

const stats = [
  { label: 'Vehicles Monitored', value: '24', note: 'Demo fleet' },
  { label: 'Active Threats', value: '03', note: 'Mock security data' },
  { label: 'Critical Alerts', value: '01', note: 'Requires investigation' },
  { label: 'Security Score', value: '86/100', note: 'Demo risk indicator' },
];

const alerts = [
  { name: 'Unusual CAN Bus Traffic', vehicle: 'Vehicle CM-001', severity: 'High', time: '09:42 AM' },
  { name: 'ECU Authentication Failure', vehicle: 'Vehicle CM-008', severity: 'Critical', time: '09:36 AM' },
  { name: 'Gateway Connection Anomaly', vehicle: 'Vehicle CM-014', severity: 'Medium', time: '09:21 AM' },
];

function DashboardHome() {
  return (
    <>
      <section className="welcome">
        <div>
          <p className="eyebrow">VEHICLE CYBERSECURITY PLATFORM</p>
          <h2>Welcome to CyberMirror</h2>
          <p>Monitor vehicle networks, investigate threats, and explore digital-twin security.</p>
        </div>
        <div className="welcome-symbol">⌘</div>
      </section>

      <section className="stats-grid">
        {stats.map((stat) => (
          <article className="stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h2>{stat.value}</h2>
            <span>{stat.note}</span>
          </article>
        ))}
      </section>

      <section className="content-grid">
        <article className="panel vehicle-panel">
          <div className="panel-heading">
            <div>
              <h3>Vehicle Digital Twin</h3>
              <p>Illustrative vehicle network overview</p>
            </div>
            <span className="tag">SIMULATED</span>
          </div>

          <div className="vehicle-visual">
            <div className="vehicle-icon">🚘</div>
            <div className="network-line" />
            <div className="ecu-grid">
              <div className="ecu">Engine ECU</div>
              <div className="ecu">Gateway</div>
              <div className="ecu">Brake ECU</div>
              <div className="ecu">Body ECU</div>
            </div>
          </div>

          <div className="vehicle-footer">
            <span>Vehicle ID: CM-001</span>
            <span><span className="status-dot" /> Simulated network</span>
          </div>
        </article>

        <article className="panel">
          <div className="panel-heading">
            <div>
              <h3>Risk Overview</h3>
              <p>Illustrative security score</p>
            </div>
          </div>

          <div className="risk-circle">
            <div>
              <strong>86</strong>
              <span>/ 100</span>
            </div>
          </div>

          <p className="risk-description">Demo score only</p>
          <div className="risk-bar"><div /></div>
          <p className="muted">
            This value is placeholder data, not a real ML prediction.
          </p>
        </article>
      </section>

      <section className="panel alerts-panel">
        <div className="panel-heading">
          <div>
            <h3>Recent Security Alerts</h3>
            <p>Example events for frontend development</p>
          </div>
          <NavLink to="/threats" className="view-link">
            View monitoring →
          </NavLink>
        </div>

        <div className="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>EVENT</th>
                <th>VEHICLE</th>
                <th>SEVERITY</th>
                <th>TIME</th>
              </tr>
            </thead>
            <tbody>
              {alerts.map((alert) => (
                <tr key={alert.name}>
                  <td>{alert.name}</td>
                  <td>{alert.vehicle}</td>
                  <td>
                    <span className={`severity ${alert.severity.toLowerCase()}`}>
                      {alert.severity}
                    </span>
                  </td>
                  <td>{alert.time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <footer className="footer">
        CyberMirror · Vehicle Cybersecurity Digital Twin
        <span>Frontend prototype · Mock data</span>
      </footer>
    </>
  );
}

function App() {
  const navigation = [
    { to: '/', label: '▦ Dashboard', end: true },
    { to: '/vehicles', label: '◈ Vehicle Twin' },
    { to: '/threats', label: '⌁ Threat Monitoring' },
    { to: '/alerts', label: '⚑ Security Alerts' },
    { to: '/simulation', label: '▷ Attack Simulation' },
    { to: '/risk', label: '◎ Risk Analysis' },
  ];

  return (
    <BrowserRouter>
      <div className="app">
        <aside className="sidebar">
          <div className="brand">
            <div className="brand-icon">C</div>
            <div>
              <h2>CyberMirror</h2>
              <span>VEHICLE SECURITY</span>
            </div>
          </div>

          <p className="menu-label">WORKSPACE</p>

          <nav className="navigation">
            {navigation.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.end}
                className={({ isActive }) =>
                  isActive ? 'nav-item active' : 'nav-item'
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>

          <div className="sidebar-bottom">
            <span className="status-dot" />
            Demo Environment
            <small>Mock data · Not live telemetry</small>
          </div>
        </aside>

        <main className="main-content">
          <header className="topbar">
            <div>
              <span className="breadcrumb">Workspace / CyberMirror</span>
              <h1>Security Dashboard</h1>
            </div>
            <div className="profile">
              <span className="live-dot" />
              <span>Demo Mode</span>
              <div className="avatar">CM</div>
            </div>
          </header>

          <Routes>
            <Route path="/" element={<DashboardHome />} />
            <Route path="/vehicles" element={<VehicleTwin />} />
            <Route path="/threats" element={<ThreatMonitoring />} />
            <Route path="/alerts" element={<SecurityAlerts />} />
            <Route path="/simulation" element={<AttackSimulation />} />
            <Route path="/risk" element={<RiskAnalysis />} />
            <Route path="*" element={<Dashboard />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
