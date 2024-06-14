def display_menu():
    """
    Displays the menu
    :return: None
    """
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst: list) -> list:
    """
    Prompts user for a value to append to the list and then appends it to the list.
    :param lst: list
    :return: list
    """
    value = input("Enter value to append to the list: ")
    lst.append(value)
    return lst


def handle_extend(lst: list) -> list:
    """
    Prompts the user for values to extend the list and then extends the list.
    :param lst: list
    :return: list
    """
    values = input("Enter values to extend the list (comma-separated): ").split(",")
    lst.extend(values)
    return lst


def handle_insert(lst: list) -> list:
    """
    Prompts the user for an index and a value to insert at that index.
    :param lst: list
    :return: int, any
    """
    try:
        index = int(input("Enter an index: "))
    except ValueError:
        print("Invalid index. Try again.")
        return
    else:
        value = input("Enter a value to be added at that index: ")
        lst.insert(index, value)
    return lst


def handle_remove(lst: list) -> list:
    """
    Prompts the user for a value to remove from the list. The method removes the first occurrence of the value.
    If value does not exist in the list, an informative message is printed.
    :param lst: list
    :return: list
    """
    value = input("Enter a value to be removed from the list: ")
    try:
        lst.remove(value)
    except ValueError:
        print(f"Value {value} cannot be removed. It does not exist in the list {lst}.")
        return
    return lst


def handle_pop(lst: list) -> list:
    """
    Prompts the user for an index to pop. Optional, pops the last item if left empty.
    :param lst: list
    :return: list
    """
    index_as_string = input("Enter an index to pop (leave empty to pop last item): ")

    if index_as_string == "":
        index_as_string = -1

    try:
        index = int(index_as_string)
    except ValueError:
        print("Invalid index value. Try again ...")
        return

    try:
        lst.pop(index)
    except IndexError:
        print("Index is out of range. Try again ... ")
        return
    return lst


def handle_clear(lst: list) -> list:
    """
    Removes all elements from the list.
    :param lst: list
    :return: list (empty)
    """
    lst.clear()
    return lst


def handle_index(lst: list):
    """
    Prompts the user for a value to find its index
    :param lst:  list
    :return: any, int
    """
    value = input("Enter a value to find its index: ")
    try:
        index = lst.index(value)
    except ValueError:
        print("Value does not exist in the list.")
        return None, None
    return value, index


def handle_count(lst: list):
    """
    Prompts the user for a value to count its occurrences in the list
    :param lst: list
    :return: any, int
    """
    value = input("Enter a value to count its occurrences in the list: ")
    count = lst.count(value)
    return value, count


def handle_sort(lst: list) -> list:
    """
    Sorts the list in ascending order.
    :param lst: list
    :return: list
    """
    lst.sort()
    return lst


def handle_reverse(lst: list) -> list:
    """
    Reverses the order of the list.
    :param lst: list
    :return: list
    """
    lst.reverse()
    return lst


def handle_copy(lst: list) -> list:
    """
    Creates a shallow copy of the list. Consequence list operations will be done on the user list, not on the copy.
    :param lst: list
    :return: list
    """
    copy_list = lst.copy()
    return copy_list


def print_list(operation: str, lst: list, value='', count=0, index=0) -> None:
    if operation == '1':
        print(f"Updated list: {lst}")
    elif operation == '2':
        print(f"Extended list: {lst}")
    elif operation == '3':
        print(f"Updated list after insert: {lst}")
    elif operation == '4':
        print(f"Updated list after removal: {lst}")
    elif operation == '5':
        print(f"Updated list after pop: {lst}")
    elif operation == '6':
        print(f"List is now empty: {lst}")
    elif operation == '7':
        print(f"Value {value} is found at index {index} in the list {lst}")
    elif operation == '8':
        print(f"Value {value} is found {count} times in the {lst}")
    elif operation == '9':
        print(f"Sorted list: {lst}")
    elif operation == '10':
        print(f"Reversed list: {lst}")
    elif operation == '11':
        print(f"Copied list: {lst}")


def main():
    """
    Main function to provide user interaction.
    """
    user_list = input("Enter initial list values (comma-separated): ").split(",")

    print(f"You entered: {user_list} list with {len(user_list)} elements.")
    while input("Press any key to continue with lists operations ... "):
        continue

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            user_list = handle_append(user_list)
            print_list(choice, user_list)

        elif choice == '2':
            handle_extend(user_list)
            print_list(choice, user_list)

        elif choice == '3':
            list_after_insert = handle_insert(user_list)
            if list_after_insert is not None:
                user_list = list_after_insert.copy()
                print_list(choice, user_list)

        elif choice == '4':
            list_after_remove = handle_remove(user_list)
            if list_after_remove is not None:
                user_list = list_after_remove.copy()
                print_list(choice, user_list)

        elif choice == '5':
            list_after_pop = handle_pop(user_list)
            if list_after_pop is not None:
                user_list = list_after_pop.copy()
                print_list(choice, user_list)

        elif choice == '6':
            handle_clear(user_list)
            print_list(choice, user_list)

        elif choice == '7':
            user_value, value_index = handle_index(user_list)
            if value_index is not None:
                print_list(choice, user_list, value=user_value, index=value_index)

        elif choice == '8':
            user_value, value_count = handle_count(user_list)
            print_list(choice, user_list, value=user_value, count=value_count)

        elif choice == '9':
            user_list = handle_sort(user_list)
            print_list(choice, user_list)

        elif choice == '10':
            user_list = handle_reverse(user_list)
            print_list(choice, user_list)

        elif choice == '11':
            copy_list = handle_copy(user_list)
            print_list(choice, copy_list)

        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

        while input("Press any key to continue with lists operations ... "):
            continue


if __name__ == "__main__":
    main()
