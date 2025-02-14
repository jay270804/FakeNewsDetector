import React from "react";
import Logo from "../assets/images/avatar-logo.webp";
import NeonButton from "./NeonButton";
import HoverVideoPlayer from "./HoverVideoPlayer";
import LogoVideo from "../assets/videos/bot2.mp4"

const Navbar = () => {
  return (
    <div className="fixed top-0 flex left-0 nav w-[100vw] justify-between ps-10 lg:pe-20 mobile:pe-5 pt-5 pb-5 border-[#3F4041] z-[100] ">
      <div className="flex gap-[1rem] items-center " >
        <div className="w-[100px] h-[100px] relative cursor-pointer ">
          <HoverVideoPlayer imageUrl={Logo} videoUrl={LogoVideo} />
        </div>

        <h1 className="text-[2rem] text-[#fff] font-bold uppercase text-[] ">Truthify.ai</h1>
      </div>

      <div>
         <NeonButton label="Search" path={"/search"} />
      </div>
    </div>
  );
};

export default Navbar;
