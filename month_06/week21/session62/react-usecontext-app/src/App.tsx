import "./App.css";
import { useState } from "react";
import { AppContext, type AppContextType } from "./contexts/AppContext";
import LayoutSolution from "./components/LayoutSolution";

function App() {
  const [username] = useState("Donald Knuth");
  const [theme, setTheme] = useState<"light" | "dark">("light");

  const toggleTheme = () => {
    setTheme((currentTheme) => (currentTheme === "light" ? "dark" : "light"));
  };

  // context-д өгөх утгаа бэлдэх
  const contextValue: AppContextType = { username, theme };

  return (
    <AppContext.Provider value={contextValue}>
      <div style={{ padding: "2rem" }}>
        <button onClick={toggleTheme}>Change theme ({theme})</button>
        <hr />
        <LayoutSolution>
          <p>This is main content</p>
        </LayoutSolution>
      </div>
    </AppContext.Provider>
    // <div style={{padding: '2rem'}}>
    //   <button onClick={toggleTheme}>
    //     Change Theme
    //   </button>
    //   <hr />
    //   <Layout username={username} theme={theme}>
    //     <p>This is Main Content</p>
    //   </Layout>
    // </div>
  );
}

export default App;
