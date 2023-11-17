import React, { useState } from "react";

function PostVocab(word, definition) {
  console.log('word', word);
  console.log('definition', definition);
  // const [response, setResponse] = useState(null);
  // const [error, setError] = useState(null);
  // console.log(word);
  const url = "http://127.0.0.1:5000/post_vocab/"; 
  const data = { word, definition };
  console.log(data);
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    // .then((response) => response.json())
    // .then((data) => {
    //   setResponse(data);
    // });
}

export default PostVocab;
