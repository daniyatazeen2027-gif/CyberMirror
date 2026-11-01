
import './SecurityAlerts.css';

const alertStats = [
  { label: 'Total Alerts', value: '18', note: 'Demo alert records' },
  { label: 'Critical Alerts', value: '03', note: 'Priority review' },
  { label: 'High Alerts', value: '05', note: 'Requires attention' },
  { label: 'Resolved Alerts', value: '10', note: 'Demo resolved records' },
];

const securityAlerts = [
  {
    id: 'ALT-001',
    title: 'ECU Authentication Failure',
    vehicle: 'CM-008',
    severity: 'Critical',
    time: '09:36 AM',
    status: 'Under Review',
  },
  {
    id: 'ALT-002',
    title: 'Unusual CAN Bus Traffic',
    vehicle: 'CM-001',
    severity: 'High',
    time: '09:42 AM',
    status: 'Open',
  },
  {
    id: 'ALT-003',
    title: 'Gateway Connection Anomaly',
    vehicle: 'CM-014',
    severity: 'Medium',
    time: '09:21 AM',
    status: 'Investigating',
  },
  {
    id: 'ALT-004',
    title: 'Unusual Network Activity',
    vehicle: 'CM-003',
    severity: 'Low',
    time: '09:15 AM',
    status: 'Resolved',
  },
  {
    id: 'ALT-005',
    title: 'Vehicle Communication Warning',
    vehicle: 'CM-005',
    severity: 'High',
    time: '08:58 AM',
    status: 'Open',
  },
];

function SecurityAlerts() {
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

        <span className="tag">DEMO ALERT CENTER</span>
      </section>

      <section className="alert-stats-grid">
        {alertStats.map((stat) => (
          <article className="alert-stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h3>{stat.value}</h3>
            <span>{stat.note}</span>
          </article>
        ))}
      </section>

      <section className="panel alert-list-panel">
        <div className="panel-heading">
          <div>
            <h3>Security Alert Records</h3>
            <p>Illustrative alerts from the demo vehicle fleet</p>
          </div>
          <span className="tag">MOCK DATA</span>
        </div>

        <div className="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>ALERT ID</th>
                <th>ALERT DESCRIPTION</th>
                <th>VEHICLE</th>
                <th>SEVERITY</th>
                <th>TIME</th>
                <th>STATUS</th>
              </tr>
            </thead>

            <tbody>
              {securityAlerts.map((alert) => (
                <tr key={alert.id}>
                  <td>{alert.id}</td>
                  <td>{alert.title}</td>
                  <td>{alert.vehicle}</td>
                  <td>
                    <span className={`severity ${alert.severity.toLowerCase()}`}>
                      {alert.severity}
                    </span>
                  </td>
                  <td>{alert.time}</td>
                  <td>
                    <span className={`alert-status ${alert.status.toLowerCase().replace(' ', '-')}`}>
                      {alert.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <p className="alerts-disclaimer">
        Demo environment: All alert records, timestamps and statuses
        are illustrative placeholder data.
      </p>

    </div>
  );
}

export default SecurityAlerts;
