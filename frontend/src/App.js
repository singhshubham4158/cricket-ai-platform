import { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000");

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    socket.on("live_update", (msg) => {
      console.log(msg);
      setData(msg);
    });

    return () => socket.off("live_update");
  }, []);

  return (
    <div style={{
      background: "#0f172a",
      color: "white",
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      {data ? (
        <div style={{
          background: "#1e293b",
          padding: "30px",
          borderRadius: "15px",
          textAlign: "center"
        }}>
          <h1>{data.name}</h1>
          <h2 style={{ fontSize: "2rem" }}>
            {data.score?.r}/{data.score?.w}
          </h2>
        </div>
      ) : (
        <h2>Loading live matches...</h2>
      )}
    </div>
  );
}

export default App;