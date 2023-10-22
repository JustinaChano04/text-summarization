// import "./App.css";
import { useState, useEffect } from "react";


function GetArticles(url) {
  const [user, setPosts] = useState([]);
  useEffect(() => {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network errror");
        }
        return response.json();
      })
      .then((data) => {
        // console.log(data);
        setPosts(data);
      });
      
  }, []);  
  console.log("user", user) ;
  return (user);
};
export default GetArticles;
