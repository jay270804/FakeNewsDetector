import React from "react";
import Card from "./Card";

const Page2 = () => {
  return (
    <div className="w-[100vw] h-[100vh] mt-[10rem]  ">
      <div className="flex w-full relative flex-col items-center ">
        <p className=" text-[4rem] relative left-[5rem] text-[#fff] uppercase font-bold ">
          Why should you
        </p>
        <p className=" text-[4rem] ms-[8rem] relative left-[-10rem] text-[#fff] uppercase font-bold ">
          trust us ?
        </p>
      </div>

      <div className="flex w-full relative justify-center items-center mt-[2rem] ">
        <div className="flex gap-[4rem] items-center ">
          <p className="text-[1rem] text-[#51E045] uppercase ">About us</p>

          <div className="w-[400px] relative ps-5 pe-5 ">
            <div className="absolute left-0 h-full w-[1px] bg-[#fff]"></div>
            <div className="absolute right-0 h-full w-[1px] bg-[#fff]"></div>

            <p className="text-[#fff]">
              Our AI-powered digital employees are customized to meet the unique
              needs of your industry, ensuring that every aspect of your
              business operates more efficiently, accurately, and innovatively.
            </p>
          </div>
        </div>
      </div>
      <Card />
    </div>
  );
};

export default Page2;
