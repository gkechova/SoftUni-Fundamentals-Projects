import datetime

INVALID_TASK_ID_VALUE = -1
INVALID_TASK_ID_VALUE_MESSAGE = "Invalid task id value. Id must be a positive integer."
INVALID_TASK_PRIORITY = -1
INVALID_TASK_PRIORITY_MESSAGE = "Task priority must be low, medium, or high."
INVALID_DATE_FORMAT = -1
INVALID_DATE_FORMAT_MESSAGE = "Invalid date. Date must be in the format YYYY-MM-DD."
INVALID_STATUS = -1
INVALID_STATUS_MESSAGE = "Status must be true or face (case non-sensitive)."
TASK_ID_ALREADY_EXISTS_MESSAGE = "Task with the same id already exists."


def validate_task_id(current_task_id):
    """
    Validates if input task ID is a non-negative integer value.

    Parameters:
    current_task_id (str): Task ID to be validated.

    Returns:
    int: Task ID as integer.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """

    try:
        task_id = int(current_task_id)
    except ValueError:
        return 0, INVALID_TASK_ID_VALUE, INVALID_TASK_ID_VALUE_MESSAGE

    if task_id <= 0:
        return 0, INVALID_TASK_ID_VALUE, INVALID_TASK_ID_VALUE_MESSAGE

    return task_id, 0, ""


def validate_task_priority(current_task_priority):
    """
    Validates if input task priority is valid (low, medium, or high).

    Parameters:
    current_task_priority (str): Input task priority.

    Returns:
    str: Validated task priority.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """

    current_task_priority = current_task_priority.lower()

    if current_task_priority != "low" and current_task_priority != "medium" and current_task_priority != "high":
        return current_task_priority, INVALID_TASK_PRIORITY, INVALID_TASK_PRIORITY_MESSAGE

    return current_task_priority, 0, ""


def validate_task_date(deadline_value):
    """
    Validates if input task deadline is valid date.
    TODO: may be this can be extended to include timezone

    Parameters:
    deadline_value (str): Input date as string

    Returns:
    str: Validated date in format YYYY-MM-DD
    int: Result code (0 for success).
    str: Descriptive error code message.
    """

    try:
        parsed_task_date = list(map(int, deadline_value.split("-")))

    except ValueError:
        return deadline_value, INVALID_DATE_FORMAT, INVALID_DATE_FORMAT_MESSAGE

    if len(parsed_task_date) == 3:
        try:
            validated_date = datetime.datetime(parsed_task_date[0], parsed_task_date[1], parsed_task_date[2])

        except ValueError:
            return deadline_value, INVALID_DATE_FORMAT, INVALID_DATE_FORMAT_MESSAGE
    else:
        return deadline_value, INVALID_DATE_FORMAT, INVALID_DATE_FORMAT_MESSAGE

    return deadline_value, 0, ""


def validate_task_input(current_task):
    """
    Calls validation functions for each new task input.

    Parameters:
    current_task (dict): Task which fields need to be validated.

    Returns:
    dict: Validated task.
    int: Result code (0 for success).
    str: Descriptive error code message.
    """

    # Validate task ID
    task_id, code, message = validate_task_id(current_task.get("id"))

    if code != 0:
        return current_task, code, message
    else:
        current_task.update({"id": task_id})

    # Validate and format priority
    priority, code, message = validate_task_priority(current_task.get("priority"))

    if code != 0:
        return current_task, code, message
    else:
        current_task.update({"priority": priority})

    # Validate deadline date
    parsed_date, code, message = validate_task_date(current_task.get("deadline"))

    if code != 0:
        return current_task, INVALID_DATE_FORMAT, message
    else:
        current_task.update({"deadline": parsed_date})

    return current_task, 0, ""


def check_task_id_uniqueness(tasks_lst, task_id):
    """
    Checks if a new task id already exists in the list. Returns error if new task ID is a duplicate.

    Parameters:
    tasks_lst (list of dict): The current list of tasks.
    task_id (int): The task ID to be checked for uniqueness.

    Returns:
    int: Result code (0 for uniqueness).
    str: Descriptive error code message.
    """
    for tsk in tasks_lst:

        if tsk["id"] == task_id:
            return INVALID_TASK_ID_VALUE, TASK_ID_ALREADY_EXISTS_MESSAGE

    return 0, ""
