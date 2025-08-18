import React, { useEffect, useState } from "react";

// Not using side effect
export function PostsBad() {
  const [posts, setPosts] = useState<string[]>([]);

  fetch("https://jsonplaceholder.typicode.com/posts?_limit=3")
    .then((result) => result.json())
    .then((data) => {
        console.log(data);
        setPosts(data.map((p: { title: string }) => p.title))
    });

  return (
    <ul>
      {posts.map((p, i) => (
        <li key={i}>{p}</li>
      ))}
    </ul>
  );
}

export function PostsGood() {
  const [posts, setPosts] = useState<string[]>([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts?_limit=3")
      .then((result) => result.json())
      .then((data) =>{
        console.log(data);
         setPosts(data.map((p: { title: string }) => p.title));
      });
  }, []); // dependency array

  return (
    <ul>
      {posts.map((p, i) => (
        <li key={i}>{p}</li>
      ))}
    </ul>
  );
}
