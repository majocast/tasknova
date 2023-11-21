import { useState } from 'react';
import { useLocation, Location, useNavigate} from 'react-router-dom';
import axios, {AxiosResponse} from 'axios';

type UserType = number | null;
type FormType = string | null;

//using this for type validation from FastAPI
interface UserReturn {
  name: string;
  id: number;
  email: string;
  username: string;
  password: string;
}

interface UserData {
  email: string;
  password: string;
}

interface CredentialsProps {
  userUpdate: (newUserId: UserType) => void;
}

function Credentials({ userUpdate }: CredentialsProps) {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [verify, setVerify] = useState<string>('');
  const [isButtonDisabled, setIsButtonDisabled] = useState<boolean>(true)
  const location: Location<string> = useLocation();
  const navigate = useNavigate();

  async function handleLogin(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const params: UserData = { email, password }
    const response: AxiosResponse<UserReturn> = await axios.get<UserReturn>('http://127.0.0.1:8000/user', { params })

    const dbData: UserReturn = response.data;
    console.log(dbData)
    userUpdate(dbData.id);
    navigate('/');
  }

  async function handleRegister(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if(password === verify) {
      const params: UserData = { email, password }
      const response: AxiosResponse<UserReturn> = await axios.get<UserReturn>('http://127.0.0.1:8000/user', { params })
      userUpdate(1);
      navigate('/');
    } else {
      alert('passwords do not match')
    }
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
        onSubmit={location.pathname === '/login' ? handleLogin : handleRegister} 
        className='creds-form'
      >
        <div className='form-group'>
          <input
            name='email'
            className='form-input'
            onChange={(e) => handleEmailChange(e)}
            required
          />
          <label htmlFor='email' className='form-label'>email</label>
        </div>
        <div className='form-group'>
          <input
            type='password'
            name='password'
            className='form-input'
            onChange={(e) => handlePasswordChange(e)}
            required  
          />
          <label htmlFor='password' className='form-label'>password</label>
        </div>
        {location.pathname === '/login' ?
          <button type='submit'>Login</button>
          :
          <>
            <div className='form-group'>
              <input 
                type='password'
                name='verify' 
                className='form-input' 
                onChange={(e) => handleVerifyChange(e)}
              />
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