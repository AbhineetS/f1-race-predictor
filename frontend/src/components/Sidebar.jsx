import React from 'react';
import SessionInfo from './SessionInfo';
import { Flag } from 'lucide-react';

export default function Sidebar({ sessionInfo }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-top">
        <img src="/f1-logo.svg" alt="F1 Logo" className="sidebar-logo" />
        <nav className="sidebar-nav">
          <div className="nav-item active">
            <Flag size={18} strokeWidth={2.5} />
            <span>Live Leaderboard</span>
          </div>
        </nav>
      </div>
      <div className="sidebar-bottom">
        <SessionInfo sessionInfo={sessionInfo} />
        <div className="copyright">
          © 2024 F1 Live<br/>
          All rights reserved.
        </div>
      </div>
    </aside>
  );
}
