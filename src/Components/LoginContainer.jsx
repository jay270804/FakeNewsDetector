import React, { useState } from "react";
import axios from "axios"; // Ensure axios is imported
import "./LoginContainer.css"; // Ensure your CSS file is correctly imported
import Loading from "../assets/videos/orb-chrome_yqe0id.webm";

const LoginContainer = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true); // Loading state
  const [claim, setClaim] = useState("");

  const fetchData = async () => {
    setLoading(true); // Set loading to true before starting the fetch
    try {
      const result = await axios.get(
        // Replace with your actual API endpoint
        "http://localhost:8080/public/getProduct?productType=Jacket&gender=Male"
      );

      console.log(result.data);
      setData(result.data); // Set fetched data
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false); // Set loading to false after the fetch is complete
    }
  };

  return (
    <div className="container z-[3]">
      {/* Colorful animated elements */}
      <i style={{ "--clr": "#76FF57" }}></i>
      <i style={{ "--clr": "#66FF99" }}></i>
      <i style={{ "--clr": "#22ff00" }}></i>

      {/* Login form */}
      <div className="login">
        {loading ? (
          <div className="w-full h-full">
            <video src={Loading} autoPlay loop muted></video>
          </div>
        ) : (
          <>
            <h2>Let's Find Out</h2>
            <h2>Let's Find Out</h2>

            <span className="input">
              <input
                type="text"
                placeholder="Enter your Claim"
                value={claim}
                onChange={(e) => setClaim(e.target.value)}
              />
              <span></span>
            </span>
          </>
        )}

        {/* Show fetched data (if any) */}
        {data && (
          <div className="data-container">
            <h3>Fetched Data:</h3>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  );
};

export default LoginContainer;
