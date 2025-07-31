import React from "react";
import Profile from "./Profile";

const Gallery: React.FC = () => {
  return (
    <>
      <h1>Amazing Profiles</h1>
      <Profile
        width={150}
        height={150}
        url="https://i.imgur.com/NBLz4oo.jpeg"
        alternative="Pokemon"
      />
      <Profile
        width={250}
        height={250}
        url="https://i.imgur.com/NBLz4oo.jpeg"
        alternative="Pokemon"
      />
      <Profile
        width={350}
        height={350}
        url="https://i.imgur.com/NBLz4oo.jpeg"
        alternative="Pokemon"
      />
    </>
  );
};

export default Gallery;
