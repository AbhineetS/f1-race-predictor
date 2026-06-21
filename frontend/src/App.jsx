import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch("http://127.0.0.1:8000/positions")
        .then((res) => res.json())
        .then((data) => setDrivers(data))
        .catch((err) => console.log(err));
    };

    fetchData();

    const interval = setInterval(fetchData, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="logo">
          <h1>🏎️ F1</h1>
        </div>

        <ul>
          <li className="active">🏁 Live Leaderboard</li>
        </ul>
      </aside>

      <main className="main">

        <div className="topbar">
          <div>
            <h1>F1 LIVE LEADERBOARD</h1>
            <p>Real-time race positions from OpenF1 API</p>
          </div>

          <div className="refresh-box">
            🟢 LIVE
          </div>
        </div>

        <div className="cards">

          <div className="card">
            <h4>RACE STATUS</h4>
            <h2>LIVE</h2>
          </div>

          <div className="card">
            <h4>DRIVERS</h4>
            <h2>{drivers.length}</h2>
          </div>

          <div className="card">
            <h4>P1</h4>
            <h2>{drivers[0]?.name || "--"}</h2>
          </div>

          <div className="card">
            <h4>P2</h4>
            <h2>{drivers[1]?.name || "--"}</h2>
          </div>

          <div className="card">
            <h4>P3</h4>
            <h2>{drivers[2]?.name || "--"}</h2>
          </div>

        </div>

        <div className="table-container">

          <table>

            <thead>
              <tr>
                <th>POS</th>
                <th>DRIVER</th>
                <th>TEAM</th>
                <th>NO.</th>
              </tr>
            </thead>

            <tbody>

              {drivers.map((driver, index) => (
                <tr key={index}>
                  <td>P{driver.position}</td>
                  <td>{driver.name}</td>
                  <td>{driver.team}</td>
                  <td>{driver.driver_number}</td>
                </tr>
              ))}

            </tbody>

          </table>

        </div>

      </main>
    </div>
  );
}

export default App;