import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    fetch('/api/sensor_data')
      .then((response) => response.json())
      .then((data) => setSensorData(data));
  }, []);

  return (
    <div>
      <h1>Water Quality Dashboard</h1>
      <ul>
        {sensorData.map((data, index) => (
          <li key={index}>{data}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
