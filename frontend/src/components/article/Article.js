/* eslint-disable @typescript-eslint/no-unused-vars */
import React from "react";
import useArticles from "../../hooks/useArticles";
import AddWord from "./AddWord";

function Article(url) {
  // const [showAlert, setShowAlert] = useState(false);

  // eslint-disable-next-lin
  url = "http://127.0.0.1:5000/articles";
  const { article, terms } = useArticles(url);


  return (
    <div className="articles">
      <ul>
        {article.map((arr) => (
          <div>
            <h1>{arr.title}</h1>
            <p>{arr.body}</p>
          </div>
        ))}
      </ul>
      {
        <ul>
          {terms.map((arr2) => (
            <AddWord 
              word={arr2.title} 
              definition={arr2.body} />
          ))}
        </ul>
      }
    </div>
  );
}
export default Article;
