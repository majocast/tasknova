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
          <div>TaskNova</div>
          {loggedIn ? 
            <div>
              <div>Login</div>
              <div>Register</div>
            </div>
            :
            <div>
              <p>My Space</p>
              <p>Register</p>
            </div>
          }
        </nav>
    </>
  )
}

export default NavBar