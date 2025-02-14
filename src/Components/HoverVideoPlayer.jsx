import React, { useState, useRef } from "react";

const HoverVideoPlayer = ({ imageUrl, videoUrl }) => {
  const [isHovered, setIsHovered] = useState(false);
  const videoRef = useRef(null);

  const handleMouseEnter = () => {
    setIsHovered(true);
    videoRef.current && videoRef.current.play();
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
    videoRef.current && videoRef.current.pause();
  };

  return (
    <div
      className="relative w-full h-full overflow-hidden "
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {isHovered ? (
        <video
          ref={videoRef}
          src={videoUrl}
          className="absolute inset-0 w-full h-full object-cover"
          muted
          loop
          style={{transform: 'scale(2)'}}
        />
      ) : (
        <img
          src={imageUrl}
          alt="Hover Preview"
          className="absolute inset-0 w-full h-full object-cover"
        />
      )}
    </div>
  );
};

export default HoverVideoPlayer;