/**
 * Frontend logic for the To-Do List application.
 * Handles DOM manipulation, event listeners, and API communication
 * with the Flask backend asynchronously using the Fetch API.
 */
document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    // Fetch and render initial todos on page load
    fetchTodos();

    /**
     * Event listener for adding a new task.
     * Prevents default form submission, sends data to the server,
     * and updates the UI on success.
     */
    todoForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = todoInput.value.trim();
        
        // Prevent empty submissions
        if (!text) return;

        try {
            // Send POST request to backend API
            const res = await fetch('/todos', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            
            if (res.ok) {
                const todo = await res.json();
                todoInput.value = ''; // Clear input field
                addTodoToDOM(todo, true); // Animate the new task in
            }
        } catch (err) {
            console.error('Error adding todo:', err);
        }
    });

    /**
     * Fetch all todos from the server and render them.
     */
    async function fetchTodos() {
        try {
            const res = await fetch('/todos');
            const todos = await res.json();
            
            todoList.innerHTML = ''; // Clear existing list
            todos.forEach(todo => addTodoToDOM(todo));
        } catch (err) {
            console.error('Error fetching todos:', err);
        }
    }

    /**
     * Creates and appends a single to-do item to the DOM.
     * 
     * @param {Object} todo - The todo data object (id, text, completed)
     * @param {boolean} animate - Whether to apply the entrance animation
     */
    function addTodoToDOM(todo, animate = false) {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.dataset.id = todo.id;
        
        // Disable animation for initial page load
        if (!animate) {
            li.style.animation = 'none';
            li.style.opacity = '1';
            li.style.transform = 'translateY(0)';
        }

        // Inner HTML structure with SVG icons
        li.innerHTML = `
            <div class="todo-content" onclick="toggleTodo(${todo.id}, ${!todo.completed}, this)">
                <div class="checkbox">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <span class="todo-text">${escapeHTML(todo.text)}</span>
            </div>
            <button class="delete-btn" onclick="deleteTodo(${todo.id}, this)" aria-label="Delete todo">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M19 7L18.1327 19.1425C18.0579 20.1891 17.187 21 16.1378 21H7.86224C6.81296 21 5.94208 20.1891 5.86732 19.1425L5 7M10 11V17M14 11V17M15 7V4C15 3.44772 14.5523 3 14 3H10C9.44772 3 9 3.44772 9 4V7M4 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
        `;

        if (animate) {
            todoList.prepend(li); // Add to top for new items
        } else {
            todoList.appendChild(li); // Append to bottom during load
        }
    }

    /**
     * Toggles the completion status of a to-do item.
     * Exposed globally to be used in inline event handlers.
     * 
     * @param {number} id - The task ID
     * @param {boolean} completed - The new completion status
     * @param {HTMLElement} element - The DOM element that triggered the event
     */
    window.toggleTodo = async (id, completed, element) => {
        try {
            const res = await fetch(`/todos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ completed: completed ? 1 : 0 })
            });
            
            if (res.ok) {
                const li = element.closest('.todo-item');
                li.classList.toggle('completed'); // Update UI status
                // Update the onclick handler with the new opposite state
                element.setAttribute('onclick', `toggleTodo(${id}, ${!completed}, this)`);
            }
        } catch (err) {
            console.error('Error toggling todo:', err);
        }
    };

    /**
     * Deletes a to-do item from the database and animates it out of the UI.
     * Exposed globally to be used in inline event handlers.
     * 
     * @param {number} id - The task ID to delete
     * @param {HTMLElement} btnElement - The delete button element
     */
    window.deleteTodo = async (id, btnElement) => {
        try {
            const res = await fetch(`/todos/${id}`, { method: 'DELETE' });
            
            if (res.ok) {
                const li = btnElement.closest('.todo-item');
                // Trigger exit animation
                li.style.transform = 'translateX(20px)';
                li.style.opacity = '0';
                // Remove from DOM after animation completes
                setTimeout(() => li.remove(), 300);
            }
        } catch (err) {
            console.error('Error deleting todo:', err);
        }
    };

    /**
     * Helper function to escape HTML characters and prevent XSS attacks.
     * 
     * @param {string} str - Raw input string
     * @returns {string} - Escaped safe string
     */
    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag])
        );
    }
});
