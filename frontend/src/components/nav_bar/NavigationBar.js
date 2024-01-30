import React from 'react';

function NavigationBar() {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li><a href="search">Search</a></li>
        <li><a href="today-summaries">Today's Summaries</a></li>
        <li><a href="all-words">All Words</a></li>
      </ul>
    </nav>
  );
}

export default NavigationBar;