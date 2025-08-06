import React, { useState } from "react";

const FocusableInput: React.FC = () => {
  const [isFocused, setIsFocused] = useState<boolean>(false);
  const dynamicStyles = {
    padding: "8px",
    border: "1px solid #ccc",
    borderRadius: "4px",
    transition: "all 0.3s",
    backgroudColor: isFocused ? "#e0f7fa" : "#ffffff",
    boxShadow: isFocused ? "0 0 5px rgba(0, 150, 200, 0.5)" : "none",
  };
  const handleFocus = (event: React.FocusEvent<HTMLInputElement>) => {
    console.log(`${event.target.id} gained focus.`);
    setIsFocused(true);
  }
  const handleBlur = (event: React.FocusEvent<HTMLInputElement>) => {
    console.log(`${event.target.id} lost focus.`);
    setIsFocused(false);
  }

  return (
    <>
      <h3>OnFocus/ onBlur Example</h3>
      <input
        type="text"
        id="focusable-input"
        placeholder="Click here to focus"
        onFocus={handleFocus}
        onBlur={handleBlur}
        style={dynamicStyles}
      />
    </>
  );
};

export default FocusableInput;
