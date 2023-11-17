import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    setLoggedIn(false)
  }, [])

  return (
    <>
      <nav>
          <Link to='/'>TaskNova</Link>
          {loggedIn ? 
            <div>
              <Link to={`/space/1`}>My Space</Link>
              <Link to={`/account/1`}>Account</Link>
            </div>
            :
            <div>
              <Link to={`/login`}>Login</Link>
              <Link to={`/register`}>Get Started</Link>
            </div>
          }
        </nav>
    </>
  )
}

export default NavBar