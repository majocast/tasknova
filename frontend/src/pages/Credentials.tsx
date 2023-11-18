import { useLocation, Location, useNavigate} from 'react-router-dom';

type UserType = number | null;

interface CredentialsProps {
  userUpdate: (newUserId: UserType) => void;
}

function Credentials({ userUpdate }: CredentialsProps) {
  const location: Location<string> = useLocation();
  const navigate = useNavigate();

  console.log(location.pathname)

  function setLogin() {
    userUpdate(1);
    navigate('/');
  }

  return (
    <>
      {location.pathname === '/login' ?
        <button onClick={setLogin}>Login</button>
        :
        <button onClick={setLogin}>Register</button>
      }
    </>
  )
}

export default Credentials;