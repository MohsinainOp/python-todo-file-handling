Persistent To-Do List Manager

A robust, lightweight To-Do List application featuring automatic file handling. This program ensures that all your tasks are safely stored to your local disk and automatically reloaded the next time the program starts, so you never lose your progress.

Features

1. Add Tasks: Create new tasks on the fly.
2. View Tasks: Display your current pending and completed to-do items.
3. Mark as Complete: Keep track of what you've accomplished.
4. Delete Tasks: Remove tasks you no longer need.
5. Persistent Storage: Automatically saves your data to a local file (tasks.txt or JSON) and loads it up instantly upon startup.

Getting Started

Prerequisites
Make sure you have your programming environment installed (e.g., Python, Node.js, C++, etc.).

Installation and Running

1. Clone this repository:
git clone https://github.com/MohsinainOp/python-todo-file-handling.git

2. Navigate into the project directory:
cd python-todo-file-handling

3. Run the application:
# Replace with your specific run command (e.g., python main.py)

How File Handling Works
When tasks are added or modified, the application writes the current state directly to a local storage file. When launched, it checks for this file, reads the data back into memory, and restores your list instantly.
