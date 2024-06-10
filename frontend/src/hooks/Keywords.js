function Keywords(keywords) {
    console.log(keywords);
    const url = "http://127.0.0.1:5000/keywords"; 
    const data = {keywords};
  
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
  }
  
  export default Keywords;
  