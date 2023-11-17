import { useEffect, useState } from 'react';
import './App.css'
import NavBar from './components/NavBar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Credentials from './pages/Credentials';
import MySpace from './pages/MySpace';
import Account from './pages/Account';

type userType = number | null;

function App() {
  const [user_id, setUser_id] = useState<userType>(null);

  useEffect(() => {
    setUser_id(1)
  }, [])

  return (
    <BrowserRouter>
      <div className='app'>
        <NavBar user_id={user_id}/>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Credentials />} />
          <Route path='/register' element={<Credentials />} />
          <Route path={`/myspace/:${user_id}`} element={<MySpace />} />
          <Route path={`/account/:${user_id}`} element={<Account />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
