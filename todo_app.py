"""
Feature: To-Do List Application Module.

This file contains the core functionality for the To-Do List application,
including the Flask app configuration, database setup, and API routes.
"""

import sqlite3
from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define the SQLite database filename
DATABASE = 'todos.db'


def get_db():
    """
    Establish a connection to the SQLite database.

    Returns:
        sqlite3.Connection: Database connection object configured to return
                            rows as dictionaries (sqlite3.Row).
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initialize the database table.
    """
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
            )
        ''')
        db.commit()


# Ensure the database is initialized on module import
init_db()


@app.route('/')
def index():
    """
    Serve the main frontend application.
    """
    return render_template('index.html')


@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Retrieve all to-do items from the database.
    """
    db = get_db()
    todos = db.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    return jsonify([dict(todo) for todo in todos])


@app.route('/todos', methods=['POST'])
def add_todo():
    """
    Create a new to-do item.
    """
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    db = get_db()
    cursor = db.execute(
        'INSERT INTO todos (text, completed) VALUES (?, 0)',
        (text,)
    )
    db.commit()
    
    return jsonify({'id': cursor.lastrowid, 'text': text, 'completed': 0}), 201


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update the completion status of a specific to-do item.
    """
    completed = request.json.get('completed')
    if completed is None:
        return jsonify({'error': 'Completed status is required'}), 400

    db = get_db()
    db.execute(
        'UPDATE todos SET completed = ? WHERE id = ?',
        (int(completed), todo_id)
    )
    db.commit()
    
    return jsonify({'success': True})


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Delete a specific to-do item.
    """
    db = get_db()
    db.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    db.commit()
    
    return jsonify({'success': True})


def start_todo_server():
    """
    Run the Flask development server on port 5001.
    """
    app.run(debug=True, port=5001)
