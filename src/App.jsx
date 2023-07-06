import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// import './App.css'
import Navbar from './Navbar'
import Slider from './Slider'
import FooterInput from './Footer';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<><Navbar /><Slider /></>} />
          <Route path="/input" element={<><Navbar /><FooterInput /></>} />
        </Routes>
      </div>
    </Router>
    // <>
    //   <Example />
    //   <Slider />
    //   {/* <FormExample6 /> */}
    // </>
  )
}

export default App
