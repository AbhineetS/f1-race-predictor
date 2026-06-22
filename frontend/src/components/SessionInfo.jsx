import React from 'react';

export default function SessionInfo({ sessionInfo }) {
  if (!sessionInfo) return <div className="session-info">Loading...</div>;

  return (
    <div className="session-info">
      <div className="session-info-header">
        <span className="session-info-title">Session Info</span>
        <div className="live-status">
          <span className="live-dot"></span> LIVE
        </div>
      </div>
      
      <div className="gp-name">{sessionInfo.meeting_name}</div>
      <div className="circuit-name">
        {sessionInfo.country_flag ? (
          <img src={sessionInfo.country_flag} alt="flag" style={{width: 16, height: 11, objectFit: 'cover', borderRadius: 2, marginRight: 6}} />
        ) : (
          <span>📍</span>
        )} {sessionInfo.circuit_short_name}
      </div>
      
      <div style={{ marginBottom: '16px' }}>
        <div style={{ color: 'var(--text-muted)', marginBottom: '4px' }}>{sessionInfo.session_name}</div>
        <div style={{ fontWeight: 600, color: '#fff' }}>Lap {sessionInfo.lap_number}</div>
      </div>
      
      <div className="session-stats-grid">
        <div className="stat-sm">
          <span className="stat-sm-label">Air Temp</span>
          <span className="stat-sm-val">{sessionInfo.air_temperature}°C</span>
        </div>
        <div className="stat-sm">
          <span className="stat-sm-label">Track Temp</span>
          <span className="stat-sm-val">{sessionInfo.track_temperature}°C</span>
        </div>
        <div className="stat-sm">
          <span className="stat-sm-label">Humidity</span>
          <span className="stat-sm-val">{sessionInfo.humidity}%</span>
        </div>
        <div className="stat-sm">
          <span className="stat-sm-label">Wind</span>
          <span className="stat-sm-val">{sessionInfo.wind_speed} m/s</span>
        </div>
      </div>
    </div>
  );
}
