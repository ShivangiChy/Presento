/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/

/*
import React, {useState} from 'react'
import axios from 'axios'

//const [image,setImage] = useState([])
function App(){
  const [image, setImage] = useState([]);

  const getImage =()=>{
    axios.get('https://api.unsplash.com/search/photos?page=1&query=books&client_id=xv0mdYsTIpNkvDZruoOHSAHiQt5h-AhuYzDTQJSOdu4')
    .then((response)=>{
      //console.log(response);
      setImage(response.data.results)
    }
    )
  }
  return (
    <>
    <div className='container my-2'>
      <div className='row'>
        <div className='col-4'>
          <button className='btn btn-primary' onClick={getImage}>Get Image</button>
        </div>
      </div>
    </div>

    <div className='contanier'>
      <div className='row'>
        {
          image.map((value,index)=>{
            return (
              <div key={index} className='col-4'>
                <div className="card" style={{width: "18rem"}}>
                  <img src={value.urls.small} className="card-img-top" alt="image"/>
                </div>
              </div>
            )
          })
        }
        
      </div>
    </div>
    
    </>
    
  )
}
export default App 
*/

import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const getImage = () => {
    axios
      .get(`https://api.unsplash.com/search/photos?page=1&query=${searchTerm}&client_id=xv0mdYsTIpNkvDZruoOHSAHiQt5h-AhuYzDTQJSOdu4`)
      .then((response) => {
        setImage(response.data.results);
      });
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <>
      <div className="container my-2">
        <div className="row">
          <div className="col-4">
            <input
              type="text"
              value={searchTerm}
              onChange={handleSearchChange}
              placeholder="Enter search term"
            />
            <button className="btn btn-primary" onClick={getImage}>
              Get Image
            </button>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          {image.map((value, index) => (
            <div key={index} className="col-4">
              <div className="card" style={{ width: '18rem' }}>
                <img src={value.urls.small} className="card-img-top" alt="image" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default App;
