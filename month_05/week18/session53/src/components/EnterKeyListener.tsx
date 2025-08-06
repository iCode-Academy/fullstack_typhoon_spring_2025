import React from "react";

const EnterKeyListener = () => {
  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      alert(
        `Enter was pressed! The input value is: "${event.currentTarget.value}"`
      );
    }
  };

  return (
    <>
      <h3>On Keydown Example</h3>
      <input
        type="text"
        placeholder="Type here and press Enter"
        onKeyDown={handleKeyDown}
      />
    </>
  );
};

export default EnterKeyListener;
