import { useCallback, useEffect, useState } from 'react';
import { getAlerts } from '../services/api';
import './SecurityAlerts.css';

function formatSeverity(severity = '') {
  return severity.charAt(0).toUpperCase() + severity.slice(1).toLowerCase();
}

function formatStatus(status = '') {
  return status
    .replace(/[_-]/g, ' ')
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function formatTime(timestamp) {
  if (!timestamp) return '—';

  const date = new Date(timestamp);

  if (Number.isNaN(date.getTime())) return '—';

  return date.toLocaleString('en-IN', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}

function SecurityAlerts() {
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const loadAlerts = useCallback(async () => {
    setLoading(true);
    setError('');

    try {
      const data = await getAlerts();
      setAlerts(data);
    } catch (err) {
      setError(err.message || 'Could not load security alerts.');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadAlerts();
  }, [loadAlerts]);

  const alertStats = [
    {
      label: 'Total Alerts',
      value: alerts.length,
      note: 'Records from PostgreSQL',
    },
    {
      label: 'Critical Alerts',
      value: alerts.filter((alert) => alert.severity === 'critical').length,
      note: 'Priority review',
    },
    {
      label: 'High Alerts',
      value: alerts.filter((alert) => alert.severity === 'high').length,
      note: 'Requires attention',
    },
    {
      label: 'Resolved Alerts',
      value: alerts.filter(
        (alert) => alert.status?.toLowerCase() === 'resolved'
      ).length,
      note: 'Resolved records',
    },
  ];

  return (
    <div className="security-alerts-page">
      <section className="alerts-intro">
        <div>
          <p className="eyebrow">VEHICLE SECURITY / ALERT MANAGEMENT</p>
          <h2>Security Alerts</h2>
          <p>
            Review vehicle security alerts, understand their severity,
            and track investigation status.
          </p>
        </div>

        <span className="tag">DATABASE ALERTS</span>
      </section>

      <section className="alert-stats-grid">
        {alertStats.map((stat) => (
          <article className="alert-stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h3>{loading ? '—' : stat.value}</h3>
            <span>{stat.note}</span>
          </article>
        ))}
      </section>

      <section className="panel alert-list-panel">
        <div className="panel-heading">
          <div>
            <h3>Security Alert Records</h3>
            <p>Live records retrieved from the CyberMirror backend</p>
          </div>
          <button type="button" onClick={loadAlerts} disabled={loading}>
            {loading ? 'Loading...' : 'Refresh'}
          </button>
        </div>

        {loading && (
          <p className="alerts-disclaimer">Loading security alerts...</p>
        )}

        {error && (
          <div className="alerts-disclaimer" role="alert">
            <p>Unable to load alerts: {error}</p>
            <p>Check that FastAPI and PostgreSQL are running, then try again.</p>
          </div>
        )}

        {!loading && !error && (
          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>ALERT ID</th>
                  <th>ALERT DESCRIPTION</th>
                  <th>VEHICLE / ECU</th>
                  <th>SEVERITY</th>
                  <th>TIME</th>
                  <th>STATUS</th>
                </tr>
              </thead>

              <tbody>
                {alerts.map((alert) => {
                  const severity = formatSeverity(alert.severity);
                  const status = formatStatus(alert.status);

                  return (
                    <tr key={alert.alert_id}>
                      <td>{alert.alert_id}</td>
                      <td>{alert.description || alert.attack_type}</td>
                      <td>{alert.ecu_id}</td>
                      <td>
                        <span className={`severity ${severity.toLowerCase()}`}>
                          {severity}
                        </span>
                      </td>
                      <td>{formatTime(alert.timestamp)}</td>
                      <td>
                        <span
                          className={`alert-status ${alert.status
                            ?.toLowerCase()
                            .replace(/[_\s]+/g, '-')}`}
                        >
                          {status}
                        </span>
                      </td>
                    </tr>
                  );
                })}

                {alerts.length === 0 && (
                  <tr>
                    <td colSpan="6">No security alerts found.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <p className="alerts-disclaimer">
        Alert records are retrieved from the CyberMirror backend and PostgreSQL database.
      </p>
    </div>
  );
}

export default SecurityAlerts;
