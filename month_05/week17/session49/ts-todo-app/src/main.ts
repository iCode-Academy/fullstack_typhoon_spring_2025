// One todo
interface Todo {
    id: number;
    text: string;
    completed: boolean;
}

// many todos
const todos: Todo[] = [];

// DOM elements of HTML
// 
const form = document.getElementById('todo-form') as HTMLFormElement;
const input = document.getElementById('todo-input') as HTMLInputElement;
const list = document.getElementById('todo-list') as HTMLUListElement;

// create function to show the todos on HTML
function renderTodos(): void{
    list.innerHTML = '';
    todos.forEach((todo) => {
        const listItem = document.createElement('li');
        listItem.textContent = todo.text;
        listItem.classList.add('todo-item');
        list.appendChild(listItem);
    })
}
// create function to handle form submission
function handleFormSubmit (event: SubmitEvent): void {
    event.preventDefault();
    const newTodoText = input.value.trim();
    if(newTodoText === ''){
        return;
    }

    const newTodo: Todo = {
        id: Date.now(),
        text: newTodoText,
        completed: false
    }

    // Add new todo into todos list
    todos.push(newTodo);
    input.value = '';
    renderTodos();
}

form.addEventListener('submit', handleFormSubmit);
renderTodos();

// Challenges

// 1. Mark as Complete: li болгон дээр шинээр checkbox үүсгэнэ. Түүндээ event listener
// нэмээд хэрвээ checkbox-ийг идэвхижүүлвэл complete болгож харуулна буюу
// дундуур зураастай болгоно.

// 2. Delete a To-Do: Delete гэдэг button Todo болгон дээр нэмээд түүнийгээ 
// дарах юм бол тухайн TODOнь устдаг байна. 

// 3. Persist Data: Localstorage ашиглаад тухайн TODO's-ийг хадгалж шинээр
// refresh хийхэд алга болгохгүй болгоно уу.