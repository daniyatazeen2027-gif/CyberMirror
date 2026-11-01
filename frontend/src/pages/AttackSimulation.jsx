
import { useState } from 'react';
import './AttackSimulation.css';

const scenarios = [
  {
    name: 'CAN Bus Traffic Anomaly',
    description: 'Illustrative unusual vehicle communication activity.',
    category: 'Network Monitoring',
  },
  {
    name: 'ECU Authentication Warning',
    description: 'Demonstration of an ECU authentication warning.',
    category: 'Authentication',
  },
  {
    name: 'Gateway Connection Anomaly',
    description: 'Illustrative gateway connection irregularity.',
    category: 'Gateway Monitoring',
  },
];

function AttackSimulation() {
  const [vehicle, setVehicle] = useState('CM-001');
  const [scenario, setScenario] = useState('CAN Bus Traffic Anomaly');
  const [status, setStatus] = useState('Ready');
  const [result, setResult] = useState(
    'Select a scenario and start the demonstration.'
  );

  const selectedScenario = scenarios.find(
    (item) => item.name === scenario
  );

  function startDemo() {
    setStatus('Demo Completed');
    setResult(
      `${scenario} demonstration completed for vehicle ${vehicle}. This is a simulated result only.`
    );
  }

  function resetDemo() {
    setStatus('Ready');
    setResult('Select a scenario and start the demonstration.');
    setVehicle('CM-001');
    setScenario('CAN Bus Traffic Anomaly');
  }

  return (
    <div className="simulation-page">

      <section className="simulation-intro">
        <div>
          <p className="eyebrow">VEHICLE SECURITY / SIMULATION LAB</p>
          <h2>Attack Simulation</h2>
          <p>
            Explore illustrative vehicle cybersecurity scenarios
            in a controlled demonstration environment.
          </p>
        </div>
        <span className="tag">DEMO ENVIRONMENT</span>
      </section>

      <section className="simulation-warning">
        <span className="status-dot" />
        Frontend demonstration only — no real vehicle or network activity.
      </section>

      <section className="simulation-layout">

        <article className="panel simulation-controls">
          <div className="panel-heading">
            <div>
              <h3>Simulation Configuration</h3>
              <p>Choose an illustrative demonstration scenario</p>
            </div>
          </div>

          <label htmlFor="vehicle-select">Select Vehicle</label>
          <select
            id="vehicle-select"
            value={vehicle}
            onChange={(e) => setVehicle(e.target.value)}
          >
            <option value="CM-001">Vehicle CM-001</option>
            <option value="CM-003">Vehicle CM-003</option>
            <option value="CM-008">Vehicle CM-008</option>
            <option value="CM-014">Vehicle CM-014</option>
          </select>

          <label htmlFor="scenario-select">Select Scenario</label>
          <select
            id="scenario-select"
            value={scenario}
            onChange={(e) => setScenario(e.target.value)}
          >
            {scenarios.map((item) => (
              <option key={item.name} value={item.name}>
                {item.name}
              </option>
            ))}
          </select>

          <div className="scenario-description">
            <span>SCENARIO DESCRIPTION</span>
            <p>{selectedScenario.description}</p>
            <small>Category: {selectedScenario.category}</small>
          </div>

          <div className="simulation-buttons">
            <button onClick={startDemo}>
              Start Demo
            </button>
            <button className="reset-button" onClick={resetDemo}>
              Reset
            </button>
          </div>
        </article>

        <article className="panel simulation-result">
          <div className="panel-heading">
            <div>
              <h3>Simulation Status</h3>
              <p>Demonstration result overview</p>
            </div>
            <span className="tag">MOCK RESULT</span>
          </div>

          <div className="simulation-status-card">
            <span>Current Status</span>
            <h2>{status}</h2>
          </div>

          <div className="result-details">
            <span>Selected Vehicle</span>
            <strong>{vehicle}</strong>
          </div>

          <div className="result-details">
            <span>Selected Scenario</span>
            <strong>{scenario}</strong>
          </div>

          <div className="result-message">
            <h4>Demonstration Output</h4>
            <p>{result}</p>
          </div>
        </article>

      </section>

      <p className="simulation-disclaimer">
        All scenarios and results are illustrative mock data.
        No actual cybersecurity tests or vehicle operations are performed.
      </p>

    </div>
  );
}

export default AttackSimulation;
