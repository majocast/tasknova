import Lottie from 'lottie-react';
import spaceman from '../assets/spaceman.json';
import { Link } from 'react-router-dom'

function Home() {
  return (
    <>
      <section className='landing-page'>
        <article className='landing-text'>
          <h1><span>TaskNova</span> brings teams together, near and far.</h1>
          <h3>Efficient <span>project management</span> from one galaxy to the next.</h3>
          <Link className='homeLink' to='/register'>Get Started</Link>
        </article>
        <Lottie
          id='home-landing'
          animationData={spaceman}
          loop
          autoplay
        />
      </section>
      <section className='home-info'>
        
      </section>
    </>
  )
}

export default Home;