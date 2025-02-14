import React from 'react'
import Speak from '../assets/videos/speak1.webm'

const Page6 = () => {
  return (
    <div className='w-[100vw] h-[100vh] relative' >
        <div className='w-[100vw] h-[100vh] absolute '  >
            <video src={Speak} autoPlay loop muted className='w-fu;; h-full' ></video>
        </div>

        
    </div>
  )
}

export default Page6