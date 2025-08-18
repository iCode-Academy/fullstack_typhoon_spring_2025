import React, { useEffect, useState } from "react";

export function ResizeBad() {
  const [width, setWidth] = useState(window.innerWidth);

  window.addEventListener("resize", () => setWidth(window.innerWidth));

  return <h2>Width: {width}</h2>;
}


export function ResizeGood () {
    const [width, setWidth] = useState(window.innerWidth);

    useEffect(() => {
        const handleResize = () => setWidth(window.innerWidth);
        window.addEventListener('resize', handleResize);

        return () => window.removeEventListener("resize", handleResize);
    }, [])
      return <h2>Width: {width}</h2>;
}