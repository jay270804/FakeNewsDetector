import React from 'react'
import './Page1.css'
import MainVideo from '../assets/videos/hero-bg.webm'

const Page1 = () => {
  return (
    <div className=' w-[100vw] h-[100vh] relative' >

    <div className='w-[100%] h-[100%] absolute ' >
      <video src={MainVideo} className='w-full h-full object-cover' autoPlay loop muted ></video>

      <div className='absolute bottom-10 right-0 ' >
        <p className='text-[#fff] text-[5rem] font-bold uppercase me-10  ' >Unmask the lies.</p>
        <p className='translate-x-[2rem] text-[#fff] text-[5rem] font-bold uppercase  ' >trust the facts</p>
      </div>

    </div>

    </div>
  )
}

export default Page1