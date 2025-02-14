import React from "react";
import VideoSrc from "../assets/videos/bot-loop.mp4";
// import "./Page3.css";
// import AVTR from "../assets/images/avatar-logo.webp";
import AVTR from "../assets/images/pagg3AVTR.webp";
import Battery from "../assets/svgs/Battery.svg";
import Shock from "../assets/svgs/Shock.svg";
import Percentage from "../assets/svgs/Percentage.svg";
import Clock from "../assets/svgs/Clock.svg";
import Mail from "../assets/svgs/Mail.svg";
import People from "../assets/svgs/People.svg";
import Immune from "../assets/svgs/Immune.svg";
import NeonButton from "./NeonButton";

const Page3 = () => {
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

      <div className="absolute bottom-10 cursor-none z-[10] flex w-full items-center justify-center " >
        <NeonButton label={"Monica"} path={"#"}  />
      </div>

      {/* <section class="bot-section bot1">
        <div class="container">
          <div class="info-block anim show">
            <div class="name-box">
              <div class="avatar anim show">
                <img
                  class="bot"
                  src={AVTR}
                  alt="Bot"
                  width="320"
                  height="320"
                />
              </div>
              <div class="text-wrap">
                <p class="name anim show">
                  secretary <span>Monica</span>
                </p>
                <p class="price anim show">
                  $
                  <span
                    class="count-progress"
                    data-animated="true"
                    data-speed="1"
                    data-step="50"
                  >
                    20,000
                  </span>
                </p>
              </div>
            </div>
            <div class="idication-box">
              <div class="icon-wrap">
                <div class="icon lotti-anim">
                  <div class="icon-anim battery"></div>
                  <span class="icon-line top-left-line"></span>
                  <span class="icon-line top-right-line"></span>
                  <span class="icon-line bot-left-line"></span>
                  <span class="icon-line bot-right-line"></span>
                </div>
                <div class="icon lotti-anim">
                  <div class="icon-anim energy"></div>
                  <span class="icon-line top-left-line"></span>
                  <span class="icon-line top-right-line"></span>
                  <span class="icon-line bot-left-line"></span>
                  <span class="icon-line bot-right-line"></span>
                </div>
                <div class="icon lotti-anim">
                  <div class="icon-anim percentage"></div>
                  <span class="icon-line top-left-line"></span>
                  <span class="icon-line top-right-line"></span>
                  <span class="icon-line bot-left-line"></span>
                  <span class="icon-line bot-right-line"></span>
                </div>
              </div>
              <div class="loop-line">
                <img
                  src="./images/icons/loop-line.webp"
                  alt="loop-line"
                  width="824"
                  height="37"
                />
                <img
                  src="./images/icons/loop-line.webp"
                  alt="loop-line"
                  width="824"
                  height="37"
                />
              </div>
            </div>
          </div>

          <div class="block">
            <h2 class="mob-title">Bot Employee VS Human Employee</h2>
            <div class="item-wrap">
              <div class="item lotti-anim anim show">
                <div class="item-icon-wrap">
                  <div class="icon-anim secretary-icons2"></div>
                </div>
                <h2 class="title">Punctuality is guaranteed</h2>
                <p class="text">
                  <span>Unlike</span> human employees who may get stuck in
                  traffic.
                </p>
              </div>
              <div class="item lotti-anim anim show">
                <div class="item-icon-wrap">
                  <div class="icon-anim secretary-icons4"></div>
                </div>
                <h2 class="title">Does not request a salary raise</h2>
                <p class="text">
                  <span>Unlike</span> human employees who ask for a periodic
                  salary raise.
                </p>
              </div>
            </div>
            <a class="main-btn mob click-song pinBtn" href="secretary.html">
              <span class="btn-text">order secretary</span>
              <span class="icon-line top-left-line"></span>
              <span class="icon-line top-right-line"></span>
              <span class="icon-line bot-left-line"></span>
              <span class="icon-line bot-right-line"></span>
            </a>
            <div class="item-wrap">
              <div class="item lotti-anim anim show">
                <div class="item-icon-wrap">
                  <div class="icon-anim secretary-icons5"></div>
                </div>
                <h2 class="title">No disagreements or disputes</h2>
                <p class="text">
                  <span>Unlike</span> human employees who may get into arguments
                  with co-workers.
                </p>
              </div>
              <div class="item lotti-anim anim show">
                <div class="item-icon-wrap">
                  <div class="icon-anim secretary-icons6"></div>
                </div>
                <h2 class="title">Immune to illnesses</h2>
                <p class="text">
                  Reducing the risk of sick leaves,
                  <span>unlike</span> human beings.
                </p>
              </div>
            </div>
            <div class="pinBtnEnd"></div>
          </div>
        </div>

        <a class="main-btn click-song" href="secretary.html">
          <span class="btn-text">order secretary</span>
          <span class="icon-line top-left-line"></span>
          <span class="icon-line top-right-line"></span>
          <span class="icon-line bot-left-line"></span>
          <span class="icon-line bot-right-line"></span>
        </a>
      </section> */}

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
    </div>
  );
};

export default Page3;
