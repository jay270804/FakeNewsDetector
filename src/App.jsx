import React from "react";
import "./App.css";
import Page1 from "./Components/page1";
import Navbar from "./Components/Navbar";
import Page2 from "./Components/Page2";
import Page3 from "./Components/Page3";
import Page4 from "./Components/Page4";
import Page5 from "./Components/Page5";
import Page6 from "./Components/Page6";
import WebGLCanvas from "./Components/WebGLCanvas";
import Search from "./Pages/Search";
import LoginContainer from "./Components/LoginContainer";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Pages/Home";

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Search" element={<Search />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
