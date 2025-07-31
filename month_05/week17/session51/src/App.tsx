import React from "react";
import { UserStatus, UserStatus02} from "./components/UserStatus";
import { ColorStatus } from "./components/ColorStatus";
import { MailBox } from "./components/MailBox";
import TodoList from "./components/TodoList";

const App: React.FC = () => {
  const messages: string[] = ['New email 1', 'New email 2'];
  const noMessages: string[] = [];
  return (
    <>
      <h1>
        Hello, Manual React and Typescript - SPA (Single Page Application)
      </h1>
      <div className="application">
        <TodoList />
      </div>
    </>
  );
};

export default App;
