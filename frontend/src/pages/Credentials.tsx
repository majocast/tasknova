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
      <h1 className='creds-form-header'>{location.pathname === '/login' ? 'login' : 'register'}</h1>
      <form 
        onSubmit={handleSubmit} 
        className='creds-form'
      >
        <div className='form-group'>
          <input name='email' className='form-input' onChange={(e) => handleEmailChange(e)}/>
          <label htmlFor='email' className='form-label'>email</label>
        </div>
        <div className='form-group'>
          <input name='password' className='form-input' onChange={(e) => handlePasswordChange(e)}/>
          <label htmlFor='password' className='form-label'>password</label>
        </div>
        {location.pathname === '/login' ?
          <button type='submit'>Login</button>
          :
          <>
            <div className='form-group'>
              <input name='verify' className='form-input' onChange={(e) => handleVerifyChange(e)}/>
              <label htmlFor='verify' className='form-label'>verify password</label>
            </div>
            <button type='submit'>Register</button>
          </>
        }
      </form>
      <div>Login with google placeholder</div>
    </>
  )
}

export default Credentials;