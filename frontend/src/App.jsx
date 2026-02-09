import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import DiningHallPage from './pages/DiningHallPage';

export default function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dining/:hallName" element={<DiningHallPage />} />
      </Routes>
    </div>
  );
}