import GetArticles from "../../hooks/getArticles/getArticles";
import PostVocab from "../../hooks/postVocab/PostVocab";

function Article(url) {
  const { article, terms } = GetArticles(url);
  console.log(article);
  console.log(terms);

  return (
    <div>
      <ul>
        {article.map((arr) => (
          <div>
            <h1>{arr.title}</h1>
            <p>{arr.body}</p>
          </div>
        ))}
      </ul>
      <ul>
        {terms.map((arr2) => (
          <div>
            <p>
              <button onClick={() => {PostVocab(arr2.title)}}>0</button> <b>{arr2.title}</b> {arr2.body}
            </p>
          </div>
        ))}
      </ul>
    </div>
  );
}
export default Article;
