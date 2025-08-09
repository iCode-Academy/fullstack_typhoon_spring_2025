import React, { useState } from "react";

type User = {
  id: number;
  name: string;
  age: number;
};

const UserAge: React.FC = () => {
  const [user, setUser] = useState<User>({
    id: 1,
    name: "John Doe",
    age: 31,
  });
  // previous state
  const handleAgeChange = () => {
    setUser((prevUser) => ({
      ...prevUser,
      age: prevUser.age + 1,
    }));
  };
  return (
    <>
      <h2>User Age</h2>
      <p>
        <strong>Name: </strong>
        {user.name}
      </p>
      <p>
        <strong>Age: </strong>
        {user.age}
      </p>
      <button onClick={handleAgeChange}>Age Up by 1</button>
    </>
  );
};

export default UserAge;
