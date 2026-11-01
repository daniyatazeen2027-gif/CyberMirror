
import './ThreatMonitoring.css';

const threatStats = [
  { label: 'Total Events', value: '128', note: 'Demo events' },
  { label: 'High Severity', value: '08', note: 'Requires review' },
  { label: 'Medium Severity', value: '15', note: 'Under observation' },
  { label: 'Low Severity', value: '24', note: 'Informational events' },
];

const threatEvents = [
  {
    name: 'Unusual CAN Bus Traffic',
    vehicle: 'CM-001',
    severity: 'High',
    time: '09:42 AM',
  },
  {
    name: 'ECU Communication Anomaly',
    vehicle: 'CM-008',
    severity: 'Medium',
    time: '09:36 AM',
  },
  {
    name: 'Gateway Connection Event',
    vehicle: 'CM-014',
    severity: 'Low',
    time: '09:21 AM',
  },
  {
    name: 'Unusual Network Activity',
    vehicle: 'CM-003',
    severity: 'High',
    time: '09:15 AM',
  },
];

function ThreatMonitoring() {
  return (
    <div className="threat-page">
      <section className="threat-intro">
        <div>
          <p className="eyebrow">VEHICLE SECURITY / MONITORING</p>
          <h2>Threat Monitoring</h2>
          <p>
            Monitor simulated vehicle network events and identify
            unusual security activity.
          </p>
        </div>

        <span className="threat-monitor-badge">
          DEMO MONITORING
        </span>
      </section>

      <section className="threat-status-panel">
        <div className="threat-status-indicator">
          <span className="status-dot" />
          Monitoring Interface Active
        </div>
        <p>Displaying illustrative security events for frontend development.</p>
      </section>

      <section className="threat-stats-grid">
        {threatStats.map((stat) => (
          <article className="threat-stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h3>{stat.value}</h3>
            <span>{stat.note}</span>
          </article>
        ))}
      </section>

      <section className="panel threat-events-panel">
        <div className="panel-heading">
          <div>
            <h3>Recent Network Events</h3>
            <p>Illustrative vehicle security activity</p>
          </div>
          <span className="tag">SIMULATED DATA</span>
        </div>

        <div className="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>EVENT</th>
                <th>VEHICLE ID</th>
                <th>SEVERITY</th>
                <th>TIME</th>
              </tr>
            </thead>

            <tbody>
              {threatEvents.map((event, index) => (
                <tr key={index}>
                  <td>{event.name}</td>
                  <td>{event.vehicle}</td>
                  <td>
                    <span className={`severity ${event.severity.toLowerCase()}`}>
                      {event.severity}
                    </span>
                  </td>
                  <td>{event.time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <p className="threat-disclaimer">
        Note: All events and statistics are mock data.
        This interface is not connected to a live vehicle network.
      </p>
    </div>
  );
}

export default ThreatMonitoring;
