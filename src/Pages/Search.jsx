import React from "react";
import "./Search.css";
import Logo from "../assets/images/avatar-logo.webp";
import LoginContainer from "../Components/LoginContainer";
import VideoSrc from "../assets/videos/hero-bg.webm";
import LogoVideo from "../assets/videos/bot2.mp4"
import HoverVideoPlayer from "../Components/HoverVideoPlayer";


const Search = () => {
  return (
    <div className="w-[100vw] overflow-hidden h-[100vh] flex justify-center items-center ">
      <div className="fixed mt-5 pt-5 top-5  flex left-5 nav w-[100vw] justify-between ps-10 lg:pe-20 mobile:pe-5 pt-5 pb-5 border-[#3F4041]  z-[100] ">
        <div className="flex  flex-col items-center ">
          <a href="/" className="w-[100px] h-[100px] relative cursor-pointer ">
            <HoverVideoPlayer imageUrl={Logo} videoUrl={LogoVideo} />
          </a>

          <h1 className="text-[1rem] text-[#fff] font-bold uppercase text-[] ">
            Truthify.ai
          </h1>
        </div>

        {/* <div>
          <NeonButton label="Home" />
        </div> */}
      </div>
      <div className="w-full h-full absolute z-[2]">
        <div className="absolute w-full h-full bg-black/30 backdrop-blur-sm"></div>

        <video
          src={VideoSrc}
          autoPlay
          loop
          muted
          className="w-full h-full object-cover"
        ></video>
      </div>

      <LoginContainer />
    </div>
  );
};

export default Search;
