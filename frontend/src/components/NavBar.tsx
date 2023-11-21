import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';

interface MyNavBarProps {
  user_id: number | null
}

const NavBar: React.FC<MyNavBarProps> = ({ user_id }) => {
  const [hidden, setHidden] = useState<boolean>(false)
  const location = useLocation();

  useEffect(() => {
    if(location.pathname === '/login' || location.pathname === '/register') {
      setHidden(true);
    } else {
      setHidden(false);
    }
  }, [location.pathname])

  if(hidden) return null;

  return (
    <>
      <nav>
          <Link to='/'>TaskNova</Link>
          {user_id ? 
            <div>
              <Link to={`/myspace/${user_id}`}>My Space</Link>
              <Link to={`/account/${user_id}`}>Account</Link>
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