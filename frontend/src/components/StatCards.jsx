import React from 'react';
import { Flag, Timer, Sun, Navigation, Wind } from 'lucide-react';

export default function StatCards({ totalDrivers, sessionInfo }) {
  const cards = [
    { label: sessionInfo?.session_name ? sessionInfo.session_name.toUpperCase() : "SESSION", value: "LIVE", icon: <Flag size={20} color="var(--f1-red)" />, valueColor: "var(--f1-red)" },
    { label: "LAP", value: sessionInfo?.lap_number || "--", icon: <Timer size={20} color="var(--purple)" /> },
    { label: "AIR TEMP", value: sessionInfo?.air_temperature ? `${sessionInfo.air_temperature}°C` : "--°C", icon: <Sun size={20} color="var(--yellow)" /> },
    { label: "TRACK TEMP", value: sessionInfo?.track_temperature ? `${sessionInfo.track_temperature}°C` : "--°C", icon: <Navigation size={20} color="var(--blue)" className="rotate-45" /> },
    { label: "WIND", value: sessionInfo?.wind_speed ? `${sessionInfo.wind_speed} m/s` : "-- m/s", icon: <Wind size={20} color="var(--success)" /> }
  ];

  return (
    <div className="stat-cards-container">
      {cards.map((card, i) => (
        <div key={i} className="stat-card">
          <div className="stat-card-icon">{card.icon}</div>
          <div className="stat-card-content">
            <div className="stat-card-title">{card.label}</div>
            <div className="stat-card-value" style={{ color: card.valueColor || '#fff' }}>{card.value}</div>
          </div>
        </div>
      ))}
    </div>
  );
}
