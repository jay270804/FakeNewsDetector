import React from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

const ParticlesBackground = () => {
  const particlesInit = async (main) => {
    console.log("Initializing particles...");
    await loadFull(main);
    console.log("Particles initialized.");
  };

  return (
    <div style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100vh" }}>
      <Particles
        id="tsparticles"
        init={particlesInit}
        options={{
          background: {
            color: {
              value: "#111111",
            },
          },
          particles: {
            number: {
              value: 80,
            },
            color: {
              value: "#51E045",
            },
            shape: {
              type: "circle",
            },
            opacity: {
              value: 0.8,
              random: true,
            },
            size: {
              value: 5,
              random: true,
            },
            move: {
              enable: true,
              speed: 3,
              direction: "none",
              random: false,
              straight: false,
              outMode: "out",
            },
            line_linked: {
              enable: true,
              distance: 150,
              color: "#51E045",
              opacity: 0.5,
              width: 1,
            },
          },
          interactivity: {
            events: {
              onhover: {
                enable: true,
                mode: "repulse",
              },
              onclick: {
                enable: true,
                mode: "push",
              },
            },
            modes: {
              repulse: {
                distance: 100,
              },
              push: {
                particles_nb: 4,
              },
            },
          },
          detectRetina: true,
        }}
      />
    </div>
  );
};

export default ParticlesBackground;