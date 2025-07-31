import React from "react";

interface Todo {
    id: number;
    text: string;
}


const TodoList: React.FC = () => {
    const todos: Todo[] = [
        {id: 1, text: "Learn Typescript"},
        {id: 2, text: "Build a typed app"},
        {id: 3, text: 'Deploy the app'}
    ]

    // Rendering list
    const todoItems = todos.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
    ))

    return (
        <div>
            <h2>My Todo List</h2>
            <ul>{todoItems}</ul>
        </div>
    )
}

export default TodoList;