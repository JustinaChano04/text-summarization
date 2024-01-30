import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SnackbarProvider from "react-simple-snackbar";
import "./App.css";

import Article from "./components/article/Article.js";
import NavigationBar from "./components/nav_bar/NavigationBar";
import AllVocab from "./components/all_words/allVocab";
import SearchNews from "./components/search/SearchNews";

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  // const data = Article("http://127.0.0.1:5000/articles");
  return (
    <SnackbarProvider>
      <Router>
        <div>
          <NavigationBar />
          <Routes>
            <Route path="/search" element={<SearchNews />} />
            <Route path="/all-words" element={<AllVocab />} />
            <Route path="/today-summaries" element={<Article />} />
          </Routes>
        </div>
      </Router>
    </SnackbarProvider>
  );
}
export default App;
