
import './VehicleTwin.css';

const ecuModules = [
  {
    name: 'Engine ECU',
    id: 'ECU-001',
    status: 'Connected',
    description: 'Engine control module',
  },
  {
    name: 'Brake ECU',
    id: 'ECU-002',
    status: 'Connected',
    description: 'Braking control module',
  },
  {
    name: 'Body ECU',
    id: 'ECU-003',
    status: 'Connected',
    description: 'Body electronics module',
  },
  {
    name: 'Gateway',
    id: 'GW-001',
    status: 'Connected',
    description: 'Vehicle network gateway',
  },
];

function VehicleTwin() {
  return (
    <div className="twin-page">
      <section className="twin-intro">
        <div>
          <p className="eyebrow">DIGITAL TWIN / VEHICLE NETWORK</p>
          <h2>Vehicle Digital Twin</h2>
          <p>
            Explore a simulated view of vehicle components and their
            communication status.
          </p>
        </div>

        <span className="tag">DEMO ENVIRONMENT</span>
      </section>

      <section className="twin-summary">
        <article className="twin-info-card">
          <span>Vehicle ID</span>
          <h3>CM-001</h3>
          <p>Demo vehicle</p>
        </article>

        <article className="twin-info-card">
          <span>Network Type</span>
          <h3>CAN Bus</h3>
          <p>Illustrative network</p>
        </article>

        <article className="twin-info-card">
          <span>ECU Modules</span>
          <h3>{ecuModules.length}</h3>
          <p>Example components</p>
        </article>
      </section>

      <section className="panel twin-network-panel">
        <div className="panel-heading">
          <div>
            <h3>Vehicle Network Overview</h3>
            <p>Illustrative component connections</p>
          </div>
          <span className="tag">SIMULATED</span>
        </div>

        <div className="twin-network">
          <div className="twin-vehicle">🚘</div>
          <div className="twin-connection" />

          <div className="twin-ecu-grid">
            {ecuModules.map((ecu) => (
              <article className="twin-ecu-card" key={ecu.id}>
                <div className="twin-ecu-icon">◇</div>
                <h4>{ecu.name}</h4>
                <p>{ecu.id}</p>
                <span className="twin-status">
                  <span className="status-dot" />
                  {ecu.status}
                </span>
                <small>{ecu.description}</small>
              </article>
            ))}
          </div>
        </div>
      </section>

      <p className="twin-disclaimer">
        Demo data only. These component statuses are illustrative and are not
        connected to a real vehicle or live telemetry.
      </p>
    </div>
  );
}

export default VehicleTwin;
