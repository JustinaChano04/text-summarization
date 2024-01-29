import React, { useState } from "react";
import Alert from "react-bootstrap/Alert";
import useArticles from "../../hooks/useArticles";
import useVocab from "../../hooks/useVocab";
import AddWord from "./AddWord";

function Article(url) {
  const [showAlert, setShowAlert] = useState(false);
  url = "http://127.0.0.1:5000/articles";
  const { article, terms } = useArticles(url);
  console.log(article);
  console.log(terms);

  const handleClick = () => {
    // Set showAlert to true to display the alert
    setShowAlert(true);

    // Hide the alert after 3 seconds
    setTimeout(() => {
      setShowAlert(false);
    }, 3000);
  };

  return (
    <div>
      <ul>
        {article.map((arr) => (
          <div>
            <h1>{arr.title}</h1>
            <p>{arr.body}</p>
          </div>
        ))}
        ;
      </ul>
      {
        <ul>
          {terms.map((arr2) => (
            <div>
              <p>
                <button
                  onClick={() => {
                    AddWord(arr2.title, arr2.body);
                  }}
                >
                  click
                </button>
                <b>{arr2.title}</b> {arr2.body}
              </p>
            </div>
          ))}
        </ul>
      }
    </div>
  );
}
export default Article;
