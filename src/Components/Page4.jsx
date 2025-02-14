import React from 'react'
import VideoSrc from "../assets/videos/bot-loop2.mp4";
import AVTR from "../assets/images/avatar-logo.webp";
import Battery from "../assets/svgs/Battery.svg";
import Shock from "../assets/svgs/Shock.svg";
import Percentage from "../assets/svgs/Percentage.svg";
import Clock from "../assets/svgs/Clock.svg";
import Mail from "../assets/svgs/Mail.svg";
import People from "../assets/svgs/People.svg";
import Immune from "../assets/svgs/Immune.svg";
import NeonButton from "./NeonButton";

const Page4 = () => {
  return (
    <div className="w-[100vw] h-[100vh] mt-[8rem] relative ">
    <div className="w-[100%] h-[100%] absolute ">
      <video
        src={VideoSrc}
        className="w-full h-full object-cover"
        autoPlay
        loop
        muted
      ></video>
    </div>

    <div className="absolute bottom-10 z-[10] flex w-full items-center justify-center " >
      <NeonButton label={"Alita"} path={"#"} />
    </div>


    <div className="w-full pt-[8rem] flex justify-between items-center relative z-[10] ps-[5rem] pe-[5rem] ">
      <div className="flex gap-5">
        <div className="w-[100px] h-[100px] border border-[#dadada] ">
          <img src={AVTR} alt="" className="w-full h-full" />
        </div>

        <div>
          <p className=" uppercase text-[#fff] text-[2rem] ">
            {" "}
            <span className="font-bold">Secretary</span> monica
          </p>
          <p className=" uppercase text-[#51E045] text-[2.5rem] ">20,000</p>
        </div>
      </div>

      <div className="flex gap-[2rem]">
        <div className="w-[50px] h-[50px] flex justify-center items-center border border-[#dadada] ">
          <img src={Battery} alt="" className="w-[70%] h-[70%]" />
        </div>
        <div className="w-[50px] h-[50px] flex justify-center items-center border border-[#dadada] ">
          <img src={Shock} alt="" className="w-[70%] h-[70%]" />
        </div>
        <div className="w-[50px] h-[50px] flex justify-center items-center border border-[#dadada] ">
          <img src={Percentage} alt="" className="w-[70%] h-[70%]" />
        </div>
      </div>
    </div>

    <div className="w-full pt-[5rem] flex justify-between items-center relative z-[10] ps-[5rem] pe-[5rem] ">
      <div className="w-[250px] relative ps-[1rem] ">
        <div className="h-[100%] w-[1px] bg-[#fff] absolute left-0 "></div>
        <div className="h-[100%] w-[1px] bg-[#fff] absolute right-0 "></div>
        <div className="w-[20px] h-[20px]  ">
          <img src={People} alt="" />
        </div>

        <p className="text-[#fff] font-bold ">Punctuality is guaranteed</p>
        <p className="text-[#fff] text-[0.6rem] ">
          Unlike human employees who may get stuck in traffic.
        </p>
      </div>
      <div className="w-[250px] relative ps-[1rem] ">
        <div className="h-[100%] w-[1px] bg-[#fff] absolute left-0 "></div>
        <div className="h-[100%] w-[1px] bg-[#fff] absolute right-0 "></div>

        <div className="w-[20px] h-[20px]  ">
          <img src={Clock} alt="" />
        </div>

        <p className="text-[#fff] font-bold ">Punctuality is guaranteed</p>
        <p className="text-[#fff] text-[0.6rem] ">
          Unlike human employees who may get stuck in traffic.
        </p>
      </div>
    </div>
    <div className="w-full mt-[15rem] flex justify-between items-center relative z-[10] ps-[5rem] pe-[5rem] ">
      <div className="w-[250px] relative ps-[1rem] ">
        <div className="h-[100%] w-[1px] bg-[#fff] absolute left-0 "></div>
        <div className="h-[100%] w-[1px] bg-[#fff] absolute right-0 "></div>

        <div className="w-[20px] h-[20px]  ">
          <img src={Mail} alt="" />
        </div>

        <p className="text-[#fff] font-bold ">Punctuality is guaranteed</p>
        <p className="text-[#fff] text-[0.6rem] ">
          Unlike human employees who may get stuck in traffic.
        </p>
      </div>
      <div className="w-[250px] relative ps-[1rem] ">
        <div className="h-[100%] w-[1px] bg-[#fff] absolute left-0 "></div>
        <div className="h-[100%] w-[1px] bg-[#fff] absolute right-0 "></div>

        <div className="w-[20px] h-[20px]  ">
          <img src={Immune} alt="" />
        </div>

        <p className="text-[#fff] font-bold ">Punctuality is guaranteed</p>
        <p className="text-[#fff] text-[0.6rem] ">
          Unlike human employees who may get stuck in traffic.
        </p>
      </div>
    </div>
  </div>  )
}

export default Page4