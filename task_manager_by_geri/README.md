# Task Manager Fundamental Project

## Project Overview

The objective of this project is to develop a suite of Python functions for a basic task manager application and provide a user menu to interact with these functions. 

## Project Requirements

- Functionality: Implement 20 distinct functions related to task management.
- Documentation: Each function should include a docstring explaining what it does, its parameters, and its return value.
- Error Handling: Functions should include appropriate error handling to manage invalid inputs or other potential issues.
- User Menu: Provide a user menu to interact with the functions and see their functionality in action.
- Code Quality: Code should follow PEP 8 guidelines and be well-organized and readable.

# Additional Information

## Suggested Functions

### Task Creation and Management:

- add_task(tasks, task): Adds a new task to the task list.
- remove_task(tasks, task_id): Removes a task by its ID.
- update_task(tasks, task_id, updated_task): Updates an existing task.
- get_task(tasks, task_id): Retrieves a task by its ID.

### Task Attributes Management:

- set_task_priority(tasks, task_id, priority): Sets the priority of a task.
- set_task_deadline(tasks, task_id, deadline): Sets the deadline for a task.
- mark_task_as_completed(tasks, task_id): Marks a task as completed.
- set_task_description(tasks, task_id, description): Sets the description for a task.

### Task Search and Filtering:

- search_tasks_by_keyword(tasks, keyword): Searches tasks by a keyword in the description.
- filter_tasks_by_priority(tasks, priority): Filters tasks by priority.
- filter_tasks_by_status(tasks, status): Filters tasks by their completion status.
- filter_tasks_by_deadline(tasks, deadline): Filters tasks by their deadline.

### Task Statistics and Reports:

- count_tasks(tasks): Returns the total number of tasks.
- count_completed_tasks(tasks): Returns the number of completed tasks.
- count_pending_tasks(tasks): Returns the number of pending tasks.
- generate_task_summary(tasks): Generates a summary report of all tasks.

### Miscellaneous:

- save_tasks_to_file(tasks, file_path): Saves the task list to a file.
- load_tasks_from_file(file_path): Loads the task list from a file.
- sort_tasks_by_deadline(tasks): Sorts tasks by their deadline.
- sort_tasks_by_priority(tasks): Sorts tasks by their priority.

# Instructions
Download **_task_manager_by_geri_** folder and run** _task_manager.py_** in your IDE.
