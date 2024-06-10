import React from "react";
import useArticles from "../../hooks/useArticles";
import AddWord from "./AddWord";

function Article(url) {
  url = "http://127.0.0.1:5000/articles";
  const articles = useArticles(url);
  return (
    <div className="articles">
      <ul>
        {articles.map((arr) => (
          <div>
            <h1>{arr.title}</h1>
            <p>{arr.summary}</p>
            <ul>
            {arr.terms.map((arr2) => (
            <AddWord 
              word={arr2.word}  
              definition={arr2.definition} />
          ))}          
            </ul>
          </div>
        ))}
      </ul>

    </div>
  );
}
export default Article;
