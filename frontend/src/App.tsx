import './App.css'
import Lottie from 'lottie-react';
import { useState, useEffect } from 'react';
import spaceman from './assets/spaceman.json';
import NavBar from './components/NavBar';
import { Link } from 'react-router-dom';

function App() {

  return (
    <>
      <div className='app'>
        <NavBar />
        <section className='landing-page'>
          <article className='landing-text'>
            <h1><span>TaskNova</span> brings teams together, near and far.</h1>
            <h3>Efficient <span>project management</span> from one galaxy to the next.</h3>
            <button>Get Started</button>
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
