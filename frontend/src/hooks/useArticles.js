import { useState, useEffect } from "react";

function useArticles(url) {
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
  }, [url]);
  return {article,terms};
}
export default useArticles;
