import React from 'react'
import './App.css'
import Lottie from 'lottie-react';
import spaceman from './assets/spaceman.json';

function App() {

  return (
    <>
      <div className='app'>
        <section className='landing-page'>
          <article className='landing-text'>
            <h1><span>TaskNova</span> brings teams together, near and far.</h1>
            <h3>Efficient <span>project management</span> from one galaxy to the next.</h3>
          </article>
          <Lottie
            id='home-landing'
            animationData={spaceman}
            loop
            autoplay
          />
        </section>
      </div>
    </>
  )
}

export default App
