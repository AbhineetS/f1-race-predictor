import React from 'react';
import { circuitData, getDefaultCircuit } from '../utils/circuitData';

export default function CircuitOverview({ sessionInfo }) {
  if (!sessionInfo) return null;

  const shortName = sessionInfo.circuit_short_name;
  let circuitKey = Object.keys(circuitData).find(key => 
    shortName && key.toLowerCase() === shortName.toLowerCase()
  );

  if (!circuitKey) {
    if (shortName === 'Spielberg') circuitKey = 'Spielberg';
    else if (shortName === 'Monza') circuitKey = 'Monza';
    else if (shortName === 'Silverstone') circuitKey = 'Silverstone';
    else if (shortName === 'Spa-Francorchamps') circuitKey = 'Spa-Francorchamps';
    else if (shortName === 'Monte Carlo') circuitKey = 'Monte Carlo';
    else if (shortName === 'Suzuka') circuitKey = 'Suzuka';
  }

  const data = circuitKey ? circuitData[circuitKey] : getDefaultCircuit();

  return (
    <section className="circuit-overview-container">
      <div className="circuit-header">
        <h2>CIRCUIT</h2>
      </div>
      <div className="circuit-overview-content new-layout">
        
        {/* Left Side: Detailed Circuit Image */}
        <div className="circuit-image-container">
          {data.imageUrl ? (
            <img src={data.imageUrl} alt={`${data.circuit} Map`} className="circuit-image" />
          ) : (
            <div className="circuit-placeholder">Map not available</div>
          )}
        </div>
        
        {/* Right Side: Circuit Stats */}
        <div className="circuit-stats-vertical">
          
          <div className="stat-group main-stat">
            <span className="stat-label">Circuit Length</span>
            <span className="stat-value-large">{data.length}</span>
          </div>

          <div className="stat-divider"></div>

          <div className="stat-row">
            <div className="stat-group">
              <span className="stat-label">First Grand Prix</span>
              <span className="stat-value">{data.firstGp}</span>
            </div>
            <div className="stat-group">
              <span className="stat-label">Number of Laps</span>
              <span className="stat-value">{data.laps}</span>
            </div>
          </div>

          <div className="stat-divider"></div>

          <div className="stat-row">
            <div className="stat-group">
              <span className="stat-label">Fastest lap time</span>
              <span className="stat-value fastest-lap">
                {data.fastestLap && data.fastestLap.split(' ').map((part, index) => 
                  index === 0 ? <strong key={index} style={{display: 'block', fontSize: '1.25rem', marginBottom: '4px'}}>{part}</strong> : part + ' '
                )}
              </span>
            </div>
            <div className="stat-group">
              <span className="stat-label">Race Distance</span>
              <span className="stat-value">{data.distance}</span>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
