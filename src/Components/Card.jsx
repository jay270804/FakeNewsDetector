import React from "react";
import "./Card.css"; // Ensure all styles are in the CSS file or styled-components

const data = [
  {
    title: "Tailored to Your Needs",
    text: "Our digital workers are not one-size-fits-all. We understand that every business is unique, and we customize our AI solutions to fit your specific requirements and goals.",
  },
  {
    title: "Advanced AI Technology",
    text: "Leveraging the latest advancements in artificial intelligence, machine learning, and natural language processing, our digital workers can perform a wide range of tasks.",
  },
  {
    title: "Increased Productivity",
    text: "Automate routine tasks, reduce human error, and free up your human workforce for more creative and strategic endeavors. Staffex’s digital workers operate 24/7, ensuring uninterrupted productivity.",
  },
  {
    title: "Scalability and Flexibility",
    text: "As your business grows, your digital workforce can scale with you. Easily add more digital workers or enhance their capabilities without the complexities of traditional hiring.",
  }
];

const Card = () => {
  return (
    <div className="slider-block mt-[5rem] ps-10 pe-10 ">
      <div className="swiper about-slider swiper-initialized swiper-horizontal swiper-backface-hidden">
        <div className="arrow-wrap">
          <div
            className="arrow prev"
            tabIndex="0"
            role="button"
            aria-label="Previous slide"
            aria-controls="swiper-wrapper-2d5ad8b33e53dace"
            aria-disabled="false"
          ></div>
          <div
            className="arrow next swiper-button-disabled"
            tabIndex="-1"
            role="button"
            aria-label="Next slide"
            aria-controls="swiper-wrapper-2d5ad8b33e53dace"
            aria-disabled="true"
          ></div>
        </div>
        <div
          className="swiper-wrapper flex  gap-[2rem] "
          id="swiper-wrapper-2d5ad8b33e53dace"
          aria-live="polite"
        >
          {data.map((slide, index) => (
            <div
              key={index}
              className={`swiper-slide w-[600px] anim lotti-anim show ${
                index === 0
                  ? "swiper-slide-active"
                  : index === 1
                  ? "swiper-slide-next"
                  : ""
              }`}
              role="group"
              aria-label={`${index + 1} / 6`}
            >
              <div className="swiper-content   border-item">
                <span className="triangle top left"></span>
                <span className="triangle top right"></span>
                <span className="triangle bot left"></span>
                <span className="triangle bot right"></span>
                <span className="line left"></span>
                <span className="line right"></span>
                <span className="dot bot left"></span>
                <span className="dot bot right"></span>
                <div className="icon-wrap">
                  <div className={`icon-anim about-icon${index + 1}`}></div>
                </div>
                <h3 className="slide-title">{slide.title}</h3>
                <p className="text">{slide.text}</p>
              </div>
            </div>
          ))}
        </div>
        <span
          className="swiper-notification"
          aria-live="assertive"
          aria-atomic="true"
        ></span>
      </div>
    </div>
  );
};

export default Card;
