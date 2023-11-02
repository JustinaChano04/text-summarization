import { useState, useEffect } from "react";

function GetArticles(url) {
  const [article, setPosts1] = useState([]);
  const [terms, setPosts2] = useState([]);
  useEffect(() => {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network errror");
        }
        return response.json();
      })
      .then((data) => {
        setPosts1(data[0]);
        setPosts2(data[1]);
      });
  }, []);
  return {article,terms};
}
export default GetArticles;
