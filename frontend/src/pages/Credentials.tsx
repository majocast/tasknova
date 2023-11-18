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
      <form className='credsForm' action={location.pathname === '/login' ? 'GET' : 'POST'}>
        <label htmlFor='email'>email</label>
        <input name='email' />
        <label htmlFor='password'>password</label>
        <input name='password' />
        {location.pathname === '/login' ?
          <button onClick={setLogin}>Login</button>
          :
          <>
            <label></label>
            <button type='submit' onClick={setLogin}>Register</button>
          </>
        }
      </form>
    </>
  )
}

export default Credentials;