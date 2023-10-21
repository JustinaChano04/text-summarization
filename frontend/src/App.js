// import logo from './logo.svg';
import "./App.css";
import { useState, useEffect } from "react";

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

function App() {
  const [user, setPosts] = useState([]);
  console.log("try me");

  const fetchArticles = () => {
    return fetch("http://127.0.0.1:5000/load_articles")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setPosts(data);
      });
  };

  useEffect(() => {
    fetchArticles();
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/load_articles")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setPosts(data);
      });
  }, []);

  return (
    <div>
      <h1>User List</h1>
      {user.map((data) => (
         <p>
            {data.title}
         </p> 
   ))}
    </div>

    /* <ul>
        {user &&
          user.title > 0 &&
          user.map((userObj, index) => (
            <li key={userObj.title}>{userObj.body}</li>
          ))}
      </ul> */
  );
}
export default App;
