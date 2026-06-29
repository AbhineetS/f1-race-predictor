import React from 'react';

import ferrariLogo from '../assets/teams/ferrari.svg';
import mercedesLogo from '../assets/teams/mercedes.svg';
import mclarenLogo from '../assets/teams/mclaren.svg';
import redbullLogo from '../assets/teams/redbull.svg';
import astonmartinLogo from '../assets/teams/astonmartin.svg';
import williamsLogo from '../assets/teams/williams.svg';
import alpineLogo from '../assets/teams/alpine.svg';
import racingbullsLogo from '../assets/teams/racingbulls.svg';
import sauberLogo from '../assets/teams/sauber.svg';
import haasLogo from '../assets/teams/haas.svg';
import audiLogo from '../assets/teams/audi.svg';
import cadillacLogo from '../assets/teams/cadillac.svg';

const officialTeamLogos = {
  "Ferrari": ferrariLogo,
  "Mercedes": mercedesLogo,
  "McLaren": mclarenLogo,
  "Red Bull Racing": redbullLogo,
  "Aston Martin": astonmartinLogo,
  "Williams": williamsLogo,
  "Alpine": alpineLogo,
  "Racing Bulls": racingbullsLogo,
  "Sauber": sauberLogo,
  "Haas F1 Team": haasLogo,
  "Haas": haasLogo,
  "Audi": audiLogo,
  "Cadillac": cadillacLogo
};

export default function TeamLogo({ teamName, height = 24 }) {
  if (!teamName) return null;
  
  const logoUrl = officialTeamLogos[teamName];
  
  return (
    <div className="team-logo" style={{ height: height, display: 'flex', alignItems: 'center', justifySelf: 'start' }}>
      {logoUrl ? (
        <img 
          src={logoUrl} 
          alt={`${teamName} Logo`} 
          style={{ height: '100%', maxWidth: '80px', objectFit: 'contain' }}
          onError={(e) => { e.target.style.display = 'none'; }}
        />
      ) : (
        <div style={{width: 24, height: height, backgroundColor: '#333', borderRadius: '50%'}}></div>
      )}
    </div>
  );
}
