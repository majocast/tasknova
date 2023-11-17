import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

interface MyNavBarProps {
  user_id: number | null
}

const NavBar: React.FC<MyNavBarProps> = ({ user_id }) => {
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    if(user_id) setLoggedIn(true)
  }, [user_id])

  return (
    <>
      <nav>
          <Link to='/'>TaskNova</Link>
          {loggedIn ? 
            <div>
              <Link to={`/myspace/${user_id}`}>My Space</Link>
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