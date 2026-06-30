// ===============================
// CONFIG API
// ===============================
// Sửa dòng này thành API của bạn
// Ví dụ Spring Boot: http://localhost:8080/api/todos
// Ví dụ json-server: http://localhost:3000/todos
const API_BASE_URL = "http://localhost:8080/api/todos";

// ===============================
// DOM ELEMENTS
// ===============================
const todoForm = document.getElementById("todoForm");
const todoInput = document.getElementById("todoInput");
const todoList = document.getElementById("todoList");
const loading = document.getElementById("loading");
const errorBox = document.getElementById("errorBox");
const emptyState = document.getElementById("emptyState");
const searchInput = document.getElementById("searchInput");
const filterStatus = document.getElementById("filterStatus");

// ===============================
// STATE
// ===============================
let todos = [];

// ===============================
// HELPER
// ===============================
function showLoading() {
    loading.classList.remove("hidden");
}

function hideLoading() {
    loading.classList.add("hidden");
}

function showError(message) {
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
}

function hideError() {
    errorBox.textContent = "";
    errorBox.classList.add("hidden");
}

/**
 * Hàm chuẩn hóa dữ liệu.
 * Nếu API của bạn trả field khác, sửa tại đây.
 *
 * FE đang dùng format:
 * {
 *   id: number,
 *   title: string,
 *   completed: boolean
 * }
 */
function normalizeTodo(todo) {
    return {
        id: todo.id,
        title: todo.title || todo.name || todo.content || "",
        completed: todo.completed ?? todo.isDone ?? todo.done ?? false,
    };
}

// ===============================
// API FUNCTIONS
// ===============================

async function getTodos() {
    const response = await fetch("http://127.0.0.1:8000/todos");

    if (!response.ok) {
        throw new Error("Không thể lấy danh sách công việc");
    }

    const data = await response.json();

    // Nếu API trả về dạng { data: [...] }
    if (Array.isArray(data.data)) {
        return data.data.map(normalizeTodo);
    }

    // Nếu API trả về thẳng mảng [...]
    if (Array.isArray(data)) {
        return data.map(normalizeTodo);
    }

    return [];
}

async function createTodo(title) {
    const response = await fetch(API_BASE_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: title,
            completed: false,
        }),
    });

    if (!response.ok) {
        throw new Error("Không thể thêm công việc");
    }

    const data = await response.json();
    return normalizeTodo(data.data || data);
}

async function updateTodo(id, updatedData) {
    const response = await fetch(`${API_BASE_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedData),
    });

    if (!response.ok) {
        throw new Error("Không thể cập nhật công việc");
    }

    const data = await response.json();
    return normalizeTodo(data.data || data);
}

async function deleteTodo(id) {
    const response = await fetch(`${API_BASE_URL}/${id}`, {
        method: "DELETE",
    });

    if (!response.ok) {
        throw new Error("Không thể xóa công việc");
    }

    return true;
}

// ===============================
// RENDER UI
// ===============================

function getFilteredTodos() {
    const keyword = searchInput.value.trim().toLowerCase();
    const status = filterStatus.value;

    return todos.filter((todo) => {
        const matchKeyword = todo.title.toLowerCase().includes(keyword);

        const matchStatus =
            status === "ALL" ||
            (status === "DONE" && todo.completed) ||
            (status === "TODO" && !todo.completed);

        return matchKeyword && matchStatus;
    });
}

function renderTodos() {
    todoList.innerHTML = "";

    const filteredTodos = getFilteredTodos();

    if (filteredTodos.length === 0) {
        emptyState.classList.remove("hidden");
        return;
    }

    emptyState.classList.add("hidden");

    filteredTodos.forEach((todo) => {
        const li = document.createElement("li");
        li.className = `todo-item ${todo.completed ? "done" : ""}`;
        li.dataset.id = todo.id;

        li.innerHTML = `
            <input 
                type="checkbox" 
                class="toggle-checkbox" 
                ${todo.completed ? "checked" : ""}
            />

            <span class="todo-title">${todo.title}</span>

            <div class="todo-actions">
                <button class="btn-edit">Sửa</button>
                <button class="btn-delete">Xóa</button>
            </div>
        `;

        todoList.appendChild(li);
    });
}

function renderEditMode(li, todo) {
    li.innerHTML = `
        <input 
            type="checkbox" 
            class="toggle-checkbox" 
            ${todo.completed ? "checked" : ""}
        />

        <input 
            type="text" 
            class="edit-input" 
            value="${todo.title}"
        />

        <div class="todo-actions">
            <button class="btn-save">Lưu</button>
            <button class="btn-cancel">Hủy</button>
        </div>
    `;
}

// ===============================
// MAIN LOGIC
// ===============================

async function loadTodos() {
    try {
        hideError();
        showLoading();

        todos = await getTodos();
        renderTodos();
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading();
    }
}

todoForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const title = todoInput.value.trim();

    if (!title) {
        showError("Vui lòng nhập tên công việc");
        return;
    }

    try {
        hideError();

        const newTodo = await createTodo(title);
        todos.unshift(newTodo);

        todoInput.value = "";
        renderTodos();
    } catch (error) {
        showError(error.message);
    }
});

todoList.addEventListener("click", async function (event) {
    const li = event.target.closest(".todo-item");

    if (!li) return;

    const id = Number(li.dataset.id);
    const todo = todos.find((item) => item.id === id);

    if (!todo) return;

    if (event.target.classList.contains("btn-delete")) {
        const confirmDelete = confirm(
            "Bạn có chắc chắn muốn xóa công việc này không?",
        );

        if (!confirmDelete) return;

        try {
            hideError();

            await deleteTodo(id);
            todos = todos.filter((item) => item.id !== id);
            renderTodos();
        } catch (error) {
            showError(error.message);
        }
    }

    if (event.target.classList.contains("btn-edit")) {
        renderEditMode(li, todo);
    }

    if (event.target.classList.contains("btn-cancel")) {
        renderTodos();
    }

    if (event.target.classList.contains("btn-save")) {
        const editInput = li.querySelector(".edit-input");
        const newTitle = editInput.value.trim();

        if (!newTitle) {
            showError("Tên công việc không được để trống");
            return;
        }

        try {
            hideError();

            const updatedTodo = await updateTodo(id, {
                title: newTitle,
                completed: todo.completed,
            });

            todos = todos.map((item) => {
                return item.id === id ? updatedTodo : item;
            });

            renderTodos();
        } catch (error) {
            showError(error.message);
        }
    }
});

todoList.addEventListener("change", async function (event) {
    if (!event.target.classList.contains("toggle-checkbox")) return;

    const li = event.target.closest(".todo-item");
    const id = Number(li.dataset.id);
    const todo = todos.find((item) => item.id === id);

    if (!todo) return;

    try {
        hideError();

        const updatedTodo = await updateTodo(id, {
            title: todo.title,
            completed: event.target.checked,
        });

        todos = todos.map((item) => {
            return item.id === id ? updatedTodo : item;
        });

        renderTodos();
    } catch (error) {
        showError(error.message);
    }
});

searchInput.addEventListener("input", renderTodos);
filterStatus.addEventListener("change", renderTodos);

// Load dữ liệu khi mở trang
loadTodos();
