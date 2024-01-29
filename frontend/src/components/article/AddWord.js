import React, { useEffect } from "react";
import useVocab from "../../hooks/useVocab";
import { useSnackbar } from "react-simple-snackbar";

function AddWord(word, definition) {
  useVocab(word, definition);
  console.log("update");

  const [openSnackbar] = useSnackbar();

  useEffect(() => {
    // Call openSnackbar when the component is rendered
    openSnackbar('This is the content of the Snackbar.');
  }, []); // Empty dependency array ensures this effect runs only once after the initial render

  return null;
}
export default AddWord;
