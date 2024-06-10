import React, { useState } from 'react';
import Keywords from '../../hooks/Keywords';
import "../../App.css";

function SearchNews() {
  const [searchInput, setSearchInput] = useState("");
  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };
  const HandleSubmit = (e) => {
    Keywords(searchInput);
  };
  return (
    <div className="search-container">
      <h1>Search Keywords</h1>
      <form onSubmit={HandleSubmit}>
        <input
          className="search-input"
          type="text"
          value={searchInput}
          onChange={handleChange}
          placeholder="keywords..."
        />
        <input className="search-submit" type="submit" value="submit" />
      </form>
    </div>
  );
}
export default SearchNews;