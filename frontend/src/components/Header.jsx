import React from 'react';
import { Thermometer, Wind, Droplets, Flag } from 'lucide-react';

export default function Header({ sessionInfo }) {
  const isLoading = !sessionInfo || sessionInfo.error;

  const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const d = new Date(dateStr);
    const months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
    return `${d.getDate()} - ${d.getDate() + 2} ${months[d.getMonth()]} ${d.getFullYear()}`;
  };

  const dateRange = !isLoading && sessionInfo.date_start ? formatDate(sessionInfo.date_start) : "";

  return (
    <div className="f1-header">
      <div className="f1-nav-top">
        <img src="/f1-logo.svg" alt="F1 Logo" className="f1-nav-logo" />
        
        {!isLoading && (
          <div className="f1-weather-stats">
            {sessionInfo.air_temperature != null && (
              <div className="stat-item">
                <span className="stat-label"><Thermometer size={12} style={{marginRight: '4px', verticalAlign: 'middle'}}/>AIR TEMP</span>
                <span className="stat-value">{sessionInfo.air_temperature}°C</span>
              </div>
            )}
            {sessionInfo.track_temperature != null && (
              <div className="stat-item">
                <span className="stat-label"><Thermometer size={12} style={{marginRight: '4px', verticalAlign: 'middle'}}/>TRACK TEMP</span>
                <span className="stat-value">{sessionInfo.track_temperature}°C</span>
              </div>
            )}
            {sessionInfo.humidity != null && (
              <div className="stat-item">
                <span className="stat-label"><Droplets size={12} style={{marginRight: '4px', verticalAlign: 'middle'}}/>HUMIDITY</span>
                <span className="stat-value">{sessionInfo.humidity}%</span>
              </div>
            )}
            {sessionInfo.wind_speed != null && (
              <div className="stat-item">
                <span className="stat-label"><Wind size={12} style={{marginRight: '4px', verticalAlign: 'middle'}}/>WIND</span>
                <span className="stat-value">{sessionInfo.wind_speed} km/h</span>
              </div>
            )}
            {sessionInfo.lap_number != null && (
              <div className="stat-item">
                <span className="stat-label"><Flag size={12} style={{marginRight: '4px', verticalAlign: 'middle'}}/>LAP</span>
                <span className="stat-value">{sessionInfo.lap_number}</span>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="f1-meeting-info">
        {isLoading ? (
           <div style={{ display: 'flex', alignItems: 'center', height: '110px' }}>
              <div className="skeleton-box" style={{ width: '400px', height: '36px' }}></div>
           </div>
        ) : (
          <>
            <div className="f1-meeting-top">
              <span className="f1-dates">{dateRange}</span>
            </div>
            <div className="f1-meeting-title">
              {sessionInfo.country_flag && <img src={sessionInfo.country_flag} alt="Flag" className="f1-meeting-flag" />}
              {sessionInfo.meeting_name ? (
                <>
                  <span className="f1-meeting-country">{sessionInfo.country_name || sessionInfo.meeting_name}</span>
                  <span className="f1-meeting-arrow">&gt;</span>
                </>
              ) : (
                <span className="f1-meeting-country">Data Unavailable</span>
              )}
            </div>
            {sessionInfo.circuit_short_name && sessionInfo.location && (
              <div className="f1-meeting-circuit">
                {sessionInfo.circuit_short_name}, {sessionInfo.location}
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
