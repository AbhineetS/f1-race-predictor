import React from 'react';

const officialTeamLogos = {
  "Ferrari": "https://upload.wikimedia.org/wikipedia/de/c/c0/Scuderia_Ferrari_Logo.svg",
  "Mercedes": "https://upload.wikimedia.org/wikipedia/commons/9/90/Mercedes-Logo.svg",
  "McLaren": "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg",
  "Red Bull Racing": "https://upload.wikimedia.org/wikipedia/en/0/05/Red_Bull_Racing_logo.svg",
  "Aston Martin": "https://upload.wikimedia.org/wikipedia/en/8/87/Aston_Martin_Aramco_Cognizant_F1_Team_logo.svg",
  "Williams": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Williams_Racing_2020_logo.svg",
  "Alpine": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Alpine_F1_Team_Logo.svg",
  "Racing Bulls": "https://upload.wikimedia.org/wikipedia/en/1/16/Visa_Cash_App_RB_logo.svg",
  "Sauber": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Kick_Sauber_logo.svg",
  "Haas F1 Team": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Haas_F1_Team_logo.svg",
  "Haas": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Haas_F1_Team_logo.svg",
  "Audi": "https://upload.wikimedia.org/wikipedia/commons/0/04/Audi_logo.svg",
  "Cadillac": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Cadillac_logo.svg"
};

export default function TeamLogo({ teamName, width = 28, height = 28 }) {
  if (!teamName) return null;
  
  const logoUrl = officialTeamLogos[teamName];
  
  return (
    <div className="team-logo" style={{ width: width, height: height, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      {logoUrl ? (
        <img 
          src={logoUrl} 
          alt={`${teamName} Logo`} 
          style={{ width: '100%', height: '100%', objectFit: 'contain' }}
          onError={(e) => { e.target.style.display = 'none'; }}
        />
      ) : (
        <div style={{width, height, backgroundColor: '#333', borderRadius: '50%'}}></div>
      )}
    </div>
  );
}
