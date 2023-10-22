import "./App.css";
import Article from "./components/article/Article.js";

function App() {
  const data = Article("http://127.0.0.1:5000/load_articles");
  return <div>{data}</div>;
}
export default App;
