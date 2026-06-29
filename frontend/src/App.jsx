import { useEffect, useState } from "react";
import "./App.css";
import Header from "./components/Header";
import CircuitOverview from "./components/CircuitOverview";
import LeaderboardTable from "./components/LeaderboardTable";

const API_URL = import.meta.env.VITE_API_URL;

export default function App() {
  const [drivers, setDrivers] = useState([]);
  const [sessionInfo, setSessionInfo] = useState(null);
  const [lastUpdated, setLastUpdated] = useState(new Date());

  useEffect(() => {
    let timeoutId;

    const fetchData = async () => {
      try {
        const [posRes, sessionRes] = await Promise.all([
          fetch(`${API_URL}/positions`),
          fetch(`${API_URL}/session-info`)
        ]);

        const posData = await posRes.json();
        const sessionData = await sessionRes.json();

        setDrivers(posData);
        setSessionInfo(sessionData);
        setLastUpdated(new Date());
      } catch (err) {
        console.error("Failed to fetch positions:", err);
      } finally {
        timeoutId = setTimeout(fetchData, 30000);
      }
    };

    fetchData();

    return () => clearTimeout(timeoutId);
  }, []);

  return (
    <div className="app-container">
      <Header sessionInfo={sessionInfo} />
      <CircuitOverview sessionInfo={sessionInfo} />
      <main className="main-content">
        <LeaderboardTable drivers={drivers} />
      </main>
    </div>
  );
}