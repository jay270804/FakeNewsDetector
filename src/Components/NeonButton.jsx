import React from "react";
import "./NeonButton.css";

const NeonButton = ({ label, path }) => {
  return (
    <a className="anchor" href={path}>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      {label}
    </a>
  );
};

export default NeonButton;
