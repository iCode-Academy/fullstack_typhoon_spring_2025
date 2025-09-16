import React from "react";
import UserProfile from "./UserProfile";

interface HeaderProps {
  username: string;
  theme: "dark" | "light";
}

const Header: React.FC<HeaderProps> = ({ username, theme }) => {
  return (
    <header>
      <h2>Header Part</h2>
      <UserProfile username={username} theme={theme} />
    </header>
  );
};

export default Header;
