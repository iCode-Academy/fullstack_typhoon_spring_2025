import React from "react";

interface UserStatusProps {
  isLoggedIn: boolean;
}

const UserStatus: React.FC<UserStatusProps> = (props) => {
  //   object destructure
  const { isLoggedIn } = props;
  return (
    <div>{isLoggedIn ? <h2>Welcome Back!</h2> : <h2>Please Log In!</h2>}</div>
  );
};

const UserStatus02: React.FC<UserStatusProps> = (props) => {
  return <div></div>;
};

export { UserStatus, UserStatus02 };
