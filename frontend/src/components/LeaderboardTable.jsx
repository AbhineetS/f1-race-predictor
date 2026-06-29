import React from 'react';
import TeamLogo from './TeamLogo';

export default function LeaderboardTable({ drivers }) {
  const isLoading = !drivers || drivers.length === 0;

  if (isLoading) {
    return (
      <div className="table-container">
        <div className="table-scroll-wrapper">
          <table className="leaderboard-table">
            <thead>
              <tr>
                <th className="col-pos">POS.</th>
                <th className="col-no">NO.</th>
                <th className="col-driver">DRIVER</th>
                <th className="col-team">TEAM</th>
                <th className="col-laps">LAPS</th>
                <th className="col-time">TIME / RETIRED</th>
                <th className="col-pts">PTS.</th>
              </tr>
            </thead>
            <tbody>
              {Array.from({ length: 20 }).map((_, i) => (
                <tr key={i} className="skeleton-row">
                  <td style={{textAlign: 'center'}}><div className="skeleton-box" style={{ width: '30px', margin: '0 auto' }}></div></td>
                  <td style={{textAlign: 'center'}}><div className="skeleton-box" style={{ width: '30px', margin: '0 auto' }}></div></td>
                  <td>
                    <div className="driver-cell">
                      <div className="skeleton-circle"></div>
                      <div className="skeleton-box" style={{ width: '150px' }}></div>
                    </div>
                  </td>
                  <td>
                    <div className="team-cell">
                      <div className="skeleton-circle" style={{ width: '32px', height: '32px' }}></div>
                      <div className="skeleton-box" style={{ width: '120px' }}></div>
                    </div>
                  </td>
                  <td style={{textAlign: 'center'}}><div className="skeleton-box" style={{ width: '40px', margin: '0 auto' }}></div></td>
                  <td><div className="skeleton-box" style={{ width: '80px' }}></div></td>
                  <td style={{textAlign: 'center'}}><div className="skeleton-box" style={{ width: '30px', margin: '0 auto' }}></div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  // Determine which columns have valid data to show
  const showLaps = drivers.some(d => d.laps !== null && d.laps !== undefined);
  const showTime = drivers.some(d => d.time_retired !== null && d.time_retired !== undefined && d.time_retired !== "");
  const showPts = drivers.some(d => d.pts !== null && d.pts !== undefined && d.pts !== "");

  return (
    <div className="table-container">
      <div className="table-scroll-wrapper">
        <table className="leaderboard-table">
          <thead>
            <tr>
              <th className="col-pos">POS.</th>
              <th className="col-no">NO.</th>
              <th className="col-driver">DRIVER</th>
              <th className="col-team">TEAM</th>
              {showLaps && <th className="col-laps">LAPS</th>}
              {showTime && <th className="col-time">TIME / RETIRED</th>}
              {showPts && <th className="col-pts">PTS.</th>}
            </tr>
          </thead>
          <tbody>
            {drivers.map((driver) => (
              <tr key={driver.driver_number}>
                <td style={{textAlign: 'center'}}>{driver.position}</td>
                <td style={{textAlign: 'center'}}>{driver.driver_number}</td>
                <td>
                  <div className="driver-cell">
                    {driver.headshot_url ? (
                       <img src={driver.headshot_url} alt={driver.name} className="driver-headshot" onError={(e) => { e.target.style.display = 'none'; }} />
                    ) : (
                       <div className="driver-headshot" />
                    )}
                    <span className="driver-name">{driver.name}</span>
                  </div>
                </td>
                <td>
                  <div className="team-cell">
                    {driver.team_colour && (
                       <div className="team-color-stripe" style={{ backgroundColor: `#${driver.team_colour}` }}></div>
                    )}
                    <TeamLogo teamName={driver.team} height={24} />
                    <span>{driver.team}</span>
                  </div>
                </td>
                {showLaps && <td style={{textAlign: 'center'}}>{driver.laps !== null ? driver.laps : ""}</td>}
                {showTime && <td>{driver.time_retired || ""}</td>}
                {showPts && <td style={{textAlign: 'center'}}>{driver.pts || ""}</td>}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
