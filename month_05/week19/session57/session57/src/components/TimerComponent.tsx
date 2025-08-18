import React, { useEffect, useState } from "react";

export function TimerBad() {
  const [count, setCount] = useState(0);
  setInterval(() => {
    setCount((c) => c + 1);
  }, 1000);

  return <h2>Count: {count}</h2>;
}

export function TimerGood() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => setCount((c) => c + 1), 1000);
    return () => clearInterval(id);
  });
  return <h2>Count: {count}</h2>;
}
