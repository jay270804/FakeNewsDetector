import React from 'react'
import Navbar from '../Components/Navbar'
import Page1 from '../Components/page1'
import Page2 from '../Components/Page2'
import Page3 from '../Components/Page3'
import Page4 from '../Components/Page4'
import Page5 from '../Components/Page5'
import Page6 from '../Components/Page6'

const Home = () => {
  return (
    <div className='overflow-x-hidden' >
        <Navbar/>
        <Page1/>
        <Page2/>
        <Page3/>
        <Page4/>
        <Page5/>
        <Page6 />
    </div>
  )
}

export default Home