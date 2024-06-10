function useVocab(word, definition) {
  const url = "http://127.0.0.1:5000/store_vocab/"; 
  const data = { word, definition };

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
}

export default useVocab;
