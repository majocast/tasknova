import { useLocation, Location } from 'react-router-dom';

function Credentials() {
  const location: Location<string> = useLocation();
  console.log(location.pathname)
  return (
    <>
      {location.pathname === '/login' ?
        <div>Login</div>
        :
        <div>Register</div>
      }
    </>
  )
}

export default Credentials;