import React from "react";
import Vocab from "../../hooks/Vocab";
import { useSnackbar } from "react-simple-snackbar";

function AddWord({ word, definition }) {
  const [openSnackbar] = useSnackbar();

  const handleClick = () => {
    openSnackbar('"' + word + '" added successfully.');
  };

  return (
    <div>
      <p>
        <button
          onClick={() => {
            handleClick();
            Vocab(word, definition);
          }}
        >
        ✅   
        </button>
        <b>{' ' + word}</b> {definition}
      </p>
    </div>
  );
}
export default AddWord;
