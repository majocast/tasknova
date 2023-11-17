import './App.css'
import NavBar from './components/NavBar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Credentials from './pages/Credentials';

function App() {
  const routes = [
    {path: '/', component: Home},
    {path: '/login', component: Credentials},
    {path: '/register', component: Credentials}
  ]

  return (
    <BrowserRouter>
      <div className='app'>
        <NavBar />
        <Routes>
          {routes.map((route) => {
            return (<Route key={route.path} path={route.path} element={<route.component />} />)
          })}
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
