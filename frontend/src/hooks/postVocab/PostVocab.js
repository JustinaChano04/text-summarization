import React, { useState } from "react";

function PostVocab(word) {
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const url = "http://127.0.0.1:5000/post_vocab"; // Replace with your API endpoint
  const data = { word };

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      setResponse(data);
      setError(null);
    })
    .catch((error) => {
      setResponse(null);
      setError(error);
    });
}

export default PostVocab;
