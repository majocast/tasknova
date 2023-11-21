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

interface RegisterData {
  email: string;
  password: string;
  name: string;
  username: string;
}

interface CredentialsProps {
  userUpdate: (newUserId: UserType) => void;
}

function Credentials({ userUpdate }: CredentialsProps) {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [verify, setVerify] = useState<string>('');
  const [username, setUsername] = useState<string>('');
  const [name, setName] = useState<string>('');
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
      const response: AxiosResponse<UserReturn> = await axios.post<UserReturn>('http://127.0.0.1:8000/user', {
        email: email, 
        password: password, 
        name: name, 
        username: username 
      })
      const dbData: UserReturn = response.data;
      console.log(dbData);
      userUpdate(dbData.id);
      navigate('/');
    } else {
      alert('passwords do not match')
    }
  }


  //handler functions
  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  }

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  }

  const handleVerifyChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setVerify(event.target.value);
  }

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value);
  }

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
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
            <div className='form-group'>
              <input 
                type='text'
                name='username' 
                className='form-input' 
                onChange={(e) => handleUsernameChange(e)}
                required
              />
              <label htmlFor='username' className='form-label'>username</label>
            </div>
            <div className='form-group'>
              <input 
                type='text'
                name='name'
                className='form-input'
                onChange={(e) => handleNameChange(e)}
                required
              />
              <label htmlFor='name' className='form-label'>your name</label>
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