import { useState } from 'react';
import { useLocation, Location, useNavigate} from 'react-router-dom';
import axios from 'axios';

type UserType = number | null;
type FormType = string | null;

interface CredentialsProps {
  userUpdate: (newUserId: UserType) => void;
}

function Credentials({ userUpdate }: CredentialsProps) {
  const [email, setEmail] = useState<FormType>(null);
  const [password, setPassword] = useState<FormType>(null);
  const [verify, setVerify] = useState<FormType>(null);
  const location: Location<string> = useLocation();
  const navigate = useNavigate();

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    userUpdate(1);
    navigate('/');
  }

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  }

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  }

  const handleVerifyChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setVerify(event.target.value);
  }

  return (
    <>
      <h1 className='form-header'>{location.pathname === '/login' ? 'login' : 'register'}</h1>
      <form 
        onSubmit={handleSubmit} 
        className='creds-form'
      >
        <label htmlFor='email'>email</label>
        <input name='email' onChange={(e) => handleEmailChange(e)}/>
        <label htmlFor='password'>password</label>
        <input name='password' onChange={(e) => handlePasswordChange(e)}/>
        {location.pathname === '/login' ?
          <button type='submit'>Login</button>
          :
          <>
            <label htmlFor='verify'>verify password</label>
            <input name='verify' onChange={(e) => handleVerifyChange(e)}/>
            <button type='submit'>Register</button>
          </>
        }
      </form>
    </>
  )
}

export default Credentials;