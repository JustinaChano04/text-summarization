import GetArticles from "../../hooks/getArticles/getArticles";

function Article(url) {
  const data = GetArticles(url);
  console.log("articleData", data);
  return (
    <div>
      <ul>
        {data.map((arr) => (
          <div>
            <h1>{arr.title}</h1>
            <p>{arr.body}</p>
          </div>
        ))}
      </ul>
    </div>
  );
}
export default Article;
