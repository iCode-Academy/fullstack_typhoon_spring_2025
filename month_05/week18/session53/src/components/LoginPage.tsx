import React, { useState } from "react";

const LoginPage: React.FC = () => {
  // State
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);

  const login = () => {
    setIsLoggedIn(!isLoggedIn);
  };

  return (
    <>
      <h1>Login Page</h1>
      <button onClick={login}>{isLoggedIn ? "Login" : "Logout"}</button>
    </>
  );
};

export { LoginPage };
