const form = document.querySelector("#form-task");
const input = document.querySelector("#task-input");
const list = document.querySelector("#task-list");

let tasks = [];

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function addTask(text) {
    if (text === "") return;
    const task = { id: crypto.randomUUID(), text: text, done: false };
    tasks.push(task);
    saveTasks();
    renderTask()
}

function renderTask() {
    list.innerHTML = "";

    tasks.forEach((task) => {
        const li = document.createElement('li')

        const text = document.createElement
            ('span')
        text.textContent = tasks.text
        if (task.done) {
            text.style.textDecoration = "line-through"
        }


    const doneBtn = document.createElement('button')
    doneBtn.tesxtContent = tasks.done ? "Undo" : "Done"
    doneBtn.addEventListener("click", () => {
        toggletask(tasks.id);
    })

    const deleteBtn = document.createElement("button")
    deleteBtn.textContent = "Delete"
    deleteBtn.addEventListener("click", function (task) {
        deleteTask(task.id);
    })

    li.appendChild(text);
    li.appendChild(doneBtn);
    li.appendChild(deleteBtn);
    list.appendChild(li);
    })
}
function toggletask(id) {
    const task = task.find(t => t.id === id)
    if (!task) return
    task.done = !task.done
    saveTasks()
    renderTask()
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id)
    saveTasks()
    renderTask()
}



form.addEventListener("submit", (e) => {
    e.preventDefault()
    const text = input.value.trim()
    addTask(text)
    input.value = ""
})

renderTask()