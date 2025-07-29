import React from "react";
import Navbar from "./components/Navbar";
import HeroOne from "./components/HeroOne";
// typescript xml
const App: React.FC = () => {
  return (
    <>
      <h1>
        Hello, Manual React and Typescript - SPA (Single Page Application)
      </h1>
      <div className="application">
        <Navbar />
        <HeroOne />
      </div>
    </>
  );
};

export default App;
