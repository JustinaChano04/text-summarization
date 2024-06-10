import { useState, useEffect } from "react";

function useArticles(url) {
  const [article, setPosts1] = useState([]);
  useEffect(() => {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network errror");
        }
        return response.json();
      })
      .then((data) => {
        setPosts1(data);
      });
  }, [url]);
  return article;
}
export default useArticles;
