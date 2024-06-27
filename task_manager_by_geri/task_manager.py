import json
import datetime
import os

from input_validations import *

TASK_NOT_FOUND_MESSAGE = "Task is not found."
TASKS_NOT_FOUND = "No tasks were found."


def add_task(tasks_lst, task_to_add):
    """
    Adds a new task to the task list.

    Parameters:
    tasks_lst (list of dict): List with tasks.
    task_to_add (dict): New task to be added to the list.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task_to_add, code, message = validate_task_input(task_to_add)

    if code != 0:
        return tasks_lst, code, message

    # If task input values are validated, check if task_to_add ID is unique
    code, message = check_task_id_uniqueness(tasks_lst, task_to_add["id"])

    if code != 0:
        return tasks_lst, code, message

    # If task_to_add id does not exist in the list, add the task to the list
    tasks_lst.append(task_to_add)

    return tasks_lst, 0, ""


def remove_task(tasks_lst, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    tasks_lst.remove(task)

    return tasks_lst, 0, ""


def update_task(tasks_lst, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    # Validate the updated task priority
    updated_priority, code, message = validate_task_priority(updated_task['priority'])

    if code != 0:
        return tasks_lst, code, message

    # Validate the updated task deadline
    updated_deadline, code, message = validate_task_date(updated_task['deadline'])

    if code != 0:
        return tasks_lst, code, message

    task['description'] = updated_task.get('description')
    task['priority'] = updated_priority
    task['deadline'] = updated_deadline

    return tasks_lst, 0, ""


def get_task(tasks_lst, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or empty dict if not found or ID is not validated.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    validated_task_id, code, message = validate_task_id(task_id)

    if code != 0:
        return {}, code, message

    for task in tasks_lst:
        if task['id'] == validated_task_id:
            return task, 0, ""
    # Task with validated input ID does not exist in the list
    else:
        return {}, INVALID_TASK_ID_VALUE, TASK_NOT_FOUND_MESSAGE


def set_task_priority(tasks_lst, task_id, new_priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    new_priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    updated_priority, code, message = validate_task_priority(new_priority)

    if code != 0:
        return tasks_lst, code, message

    if not task:
        return tasks_lst, INVALID_TASK_ID_VALUE, TASK_NOT_FOUND_MESSAGE

    # Update the task priority after input validation
    task['priority'] = updated_priority

    return tasks_lst, 0, ""


def set_task_deadline(tasks_lst, task_id, new_deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    new_deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    validated_deadline, code, message = validate_task_date(new_deadline)

    if code != 0:
        return tasks_lst, code, message

    if not task:
        return tasks_lst, INVALID_TASK_ID_VALUE, TASK_NOT_FOUND_MESSAGE

    # Task ID and deadline is validated and task is found. Update the task deadline
    task['deadline'] = validated_deadline

    return tasks_lst, 0, ""


def mark_task_as_completed(tasks_lst, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    if not task:
        return tasks_lst, INVALID_TASK_ID_VALUE, TASK_NOT_FOUND_MESSAGE

    # Task ID is validated and task is found. Mark task as completed
    task['completed'] = True

    return tasks_lst, 0, ""


def set_task_description(tasks_lst, task_id, new_description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    new_description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    task, code, message = get_task(tasks_lst, task_id)

    if code != 0:
        return tasks_lst, code, message

    if not task:
        return tasks_lst, INVALID_TASK_ID_VALUE, TASK_NOT_FOUND_MESSAGE

    # Task ID is validated and task is found. Update the task description
    task['description'] = new_description

    return tasks_lst, 0, ""


def search_tasks_by_keyword(tasks_lst, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    found_tasks_lst = []

    for task in tasks_lst:
        if keyword in task['description']:
            found_tasks_lst.append(task)

    return found_tasks_lst


def filter_tasks_by_priority(tasks_lst, tasks_priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    tasks_priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """

    priority_filter, code, message = validate_task_priority(tasks_priority)

    if code != 0:
        return [], code, message

    filtered_tasks_by_priority = \
        filter(lambda task_with_priority: task_with_priority['priority'] == priority_filter, tasks_lst)

    return list(filtered_tasks_by_priority), 0, ""


def filter_tasks_by_status(tasks_lst, status_filter):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status_filter (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    filtered_tasks_by_completion = \
        filter(lambda task_with_status: task_with_status['completed'] == status_filter, tasks_lst)

    return list(filtered_tasks_by_completion)


def filter_tasks_by_deadline(tasks_lst, tasks_deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    tasks_deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """
    deadline_filter, code, message = validate_task_date(tasks_deadline)

    if code != 0:
        return [], code, message

    filtered_tasks_by_deadline = \
        filter(lambda task_with_deadline: task_with_deadline['deadline'] == deadline_filter, tasks_lst)

    return list(filtered_tasks_by_deadline), 0, ""


def count_tasks(tasks_lst):
    """
    Returns the total number of tasks.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """
    return len(tasks_lst)


def count_completed_tasks(tasks_lst):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """
    count_of_completed_tasks = len([task for task in tasks_lst if task['completed']])

    return count_of_completed_tasks


def count_pending_tasks(tasks_lst):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """
    count_of_pending_tasks = len([task for task in tasks_lst if not task['completed']])

    return count_of_pending_tasks


def generate_task_summary(tasks_lst):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """
    total_count_of_tasks = count_tasks(tasks_lst)
    count_of_completed_tasks = count_completed_tasks(tasks_lst)
    count_of_pending_tasks = count_pending_tasks(tasks_lst)

    generated_summary = {
                        "total": total_count_of_tasks,
                        "completed": count_of_completed_tasks,
                        "pending": count_of_pending_tasks
    }

    return str(generated_summary)


def save_tasks_to_file(tasks_lst, filepath):
    """
    Saves the task list to a file.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    filepath (str): The path to the file where tasks will be saved. Filename will consist of file creation timestamp.

    Returns:
    None
    """
    if filepath[-1] == '\\':
        filename_with_path = filepath + str(datetime.datetime.now().timestamp()) + '.txt'
    else:
        filename_with_path = filepath + '\\' + str(datetime.datetime.now().timestamp()) + '.txt'

    current_writing_file = open(filename_with_path, mode='w', encoding='utf-8')

    for task in tasks_lst:
        json.dump(task, current_writing_file)
        current_writing_file.write('\n')

    current_writing_file.close()


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The file name including the path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """
    loaded_tasks = []
    current_reading_file = open(file_path, mode='r', encoding='utf-8')

    for line in current_reading_file.readlines():

        loaded_task = json.loads(str(line), object_hook=dict)
        loaded_task, code, message = validate_task_input(loaded_task)

        if code == 0:
            loaded_tasks.append(loaded_task)
        else:
            print(f"Could not load {loaded_task} -  {message}")
            current_reading_file.close()
            loaded_tasks = []
            break
    current_reading_file.close()

    return loaded_tasks


def sort_tasks_by_deadline(tasks_lst):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    return sorted(tasks_lst, key=lambda task: task['deadline'])


def sort_tasks_by_priority(tasks_lst):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    high_priority_tasks, code, message = filter_tasks_by_priority(tasks_lst, 'high')
    medium_priority_tasks, code, message = filter_tasks_by_priority(tasks_lst, 'medium')
    low_priority_tasks, code, message = filter_tasks_by_priority(tasks_lst, 'low')

    sorted_by_priority_tasks = high_priority_tasks + medium_priority_tasks + low_priority_tasks

    return sorted_by_priority_tasks


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []

    while True:
        # [print(f"{task}") for task in tasks]
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            input_task = {
                          'id': input("Enter task ID: "),
                          'description': input("Enter task description: "),
                          'priority': input("Enter task priority (low, medium, high): "),
                          'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                          'completed': False
            }

            tasks, code, message = add_task(tasks, input_task)

            if code != 0:
                print(message)
                continue

            print("Task added successfully.")

        elif choice == '2':
            input_task_id = input("Enter task ID to remove: ")

            tasks, code, message = remove_task(tasks, input_task_id)

            if code != 0:
                print(message)
                continue

            print("Task removed successfully.")

        elif choice == '3':

            input_task_id = input("Enter task ID to update: ")
            updated_task_from_input = {
                            'description': input("Enter new task description: "),
                            'priority': input("Enter new task priority (low, medium, high): "),
                            'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }

            tasks, code, message = update_task(tasks, input_task_id, updated_task_from_input)

            if code != 0:
                print(message)
                continue

            print("Task updated successfully.")

        elif choice == '4':
            input_task_id = input("Enter task ID to get: ")

            task, code, message = get_task(tasks, input_task_id)

            if code != 0:
                print(message)
                continue

            print("Task details:", task)

        elif choice == '5':
            input_task_id = input("Enter task ID to set priority: ")
            input_priority = input("Enter new priority (low, medium, high): ")

            tasks, code, message = set_task_priority(tasks, input_task_id, input_priority)

            if code != 0:
                print(message)
                continue

            print("Task priority set successfully.")

        elif choice == '6':
            input_task_id = input("Enter task ID to set deadline: ")
            input_deadline = input("Enter new deadline (YYYY-MM-DD): ")

            tasks, code, message = set_task_deadline(tasks, input_task_id, input_deadline)

            if code != 0:
                print(message)
                continue

            print("Task deadline set successfully.")

        elif choice == '7':
            input_task_id = input("Enter task ID to mark as completed: ")

            tasks, code, message = mark_task_as_completed(tasks, input_task_id)

            if code != 0:
                print(message)
                continue

            print("Task marked as completed.")

        elif choice == '8':
            input_task_id = input("Enter task ID to set description: ")
            updated_description = input("Enter new description: ")

            tasks, code, message = set_task_description(tasks, input_task_id, updated_description)

            if code != 0:
                print(message)
                continue

            print("Task description set successfully.")

        elif choice == '9':
            keyword = input("Enter keyword to search: ")

            found_tasks = search_tasks_by_keyword(tasks, keyword)
            count_of_found_tasks = len(found_tasks)

            if count_of_found_tasks == 0:
                print(TASKS_NOT_FOUND)
            else:
                print("Tasks found:", found_tasks)
                print(f"\nTotal count: {count_of_found_tasks}")

        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")

            filtered_tasks, code, message = filter_tasks_by_priority(tasks, priority)

            if code != 0:
                print(message)
                continue

            if len(filtered_tasks) > 0:
                print("Filtered tasks:", filtered_tasks)
            else:
                print(f"There are no tasks with {priority} priority.")

        elif choice == '11':
            # invalid input is False !!!
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'

            filtered_tasks = filter_tasks_by_status(tasks, status)

            if len(filtered_tasks) > 0:
                print("Filtered tasks:\n", filtered_tasks)
            else:
                if status:
                    print("There are no tasks with 'completed' status.")
                else:
                    print("There are no tasks with 'pending' status.")

        elif choice == '12':

            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")

            filtered_tasks, code, message = filter_tasks_by_deadline(tasks, deadline)

            if code != 0:
                print(message)
                continue

            if len(filtered_tasks) > 0:
                print("Filtered tasks:\n", filtered_tasks)
            else:
                print(f"There are no tasks with deadline {deadline}.")

        elif choice == '13':

            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)

        elif choice == '14':

            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)

        elif choice == '15':

            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)

        elif choice == '16':

            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)

        elif choice == '17':

            file_path = input("Enter file path to save tasks: ")

            if os.path.exists(file_path):
                save_tasks_to_file(tasks, file_path)
                print(f"Tasks saved to file.")
            else:
                print("Path does not exist. Try again.")

        elif choice == '18':

            file_path = input("Enter file path to load tasks from: ")

            if os.path.isfile(file_path):
                tasks = load_tasks_from_file(file_path)
                if len(tasks) > 0:
                    print("Tasks loaded from file.")
            else:
                print(f"File {file_path} does not exist.")

        elif choice == '19':

            tasks = sort_tasks_by_deadline(tasks)

            print("Tasks sorted by deadline.")

        elif choice == '20':

            tasks = sort_tasks_by_priority(tasks)

            [print(f"{task}") for task in tasks]
            print("Tasks sorted by priority.")

        elif choice == '21':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
