INVALID_NAME_VALUE = "Enter a valid student name. Name cannot be empty. Try again. "
INVALID_AGE_VALUE = -1
INVALID_AGE_VALUE_MESSAGE = "The age you entered is invalid. Try again. "
INVALID_AGE_RANGE_MESSAGE = "Student age must be a positive value. Try again. "
INVALID_GRADE_VALUE = -1
INVALID_GRADE_VALUE_MESSAGE = "Invalid student grade. Grade must be a value between [2.00, 6.00]. Try again. "
STUDENT_ALREADY_EXISTS_MESSAGE = "Student already exists. Try again. "
STUDENT_NOT_FOUND = "Student is not found. Try again. "

# List of dictionaries to store all students
students = list()


def validate_student_name(name, operation):
    """
    Validates student name. If the function is called for update of an existing student, empty value is accepted.
    If the function is called to add, delete or search for a student with empty name, the user is prompted to try again.
    :param name:  Student name
    :param operation: Operation from which validation is called. Possible values are: add, update, delete, search.
    :return: str (name or error message)
    """
    if (operation == "add" or operation == "delete" or operation == "search") and name.strip() == "":
        return INVALID_NAME_VALUE

    elif operation == "update" and name.strip() == "":
        return ""

    else:
        return name


def validate_student_age(age):
    """
    Prompts for student age.
    If age is not a positive integer number the user is prompted to try again.
    :param age: Student age.
    :return: int (age), str (message)
    """
    if age == "":
        return "", ""

    else:
        try:
            age = int(age)

        except ValueError:
            return INVALID_AGE_VALUE, INVALID_AGE_VALUE_MESSAGE

        else:
            if age <= 0:
                return INVALID_AGE_VALUE, INVALID_AGE_RANGE_MESSAGE
            else:
                return age, ""


def validate_student_grade(grade_input):
    """
    Validates student grade. A valid student grade is a float number between 2.00 and 6.00.
    :param grade_input: str
    :return: float (grade), str (message)
    """
    if grade_input == "":
        return "", ""

    else:
        try:
            grade = float(grade_input)

        except ValueError:
            return INVALID_GRADE_VALUE, INVALID_GRADE_VALUE_MESSAGE

        else:
            if grade < 2.00 or grade > 6.00:
                return INVALID_GRADE_VALUE, INVALID_GRADE_VALUE_MESSAGE

            else:
                return grade, ""


def format_student_subjects(subjects):
    """
    Splits subjects into a list. Strips empty spaces, if any.
    :param subjects: student subjects (comma-separated)
    :return: list (subjects)
    """
    if subjects == "":
        listed_subjects = list()

    else:
        listed_subjects = subjects.split(',')

        for subject_index in range(len(listed_subjects)):
            listed_subjects[subject_index] = str(listed_subjects[subject_index]).strip()

    return listed_subjects


def add_student(name, age, grade, subjects):
    """
    Add a new student record. Each student is a dictionary with keys: name, age, grade, and subjects.
    :param name: The name of the student.
    :param age: The age of the student.
    :param grade: The grade of the student.
    :param subjects: list (subjects the student is enrolled in)
    :return:
    """
    for current_student in students:

        if current_student["name"] == name:
            return STUDENT_ALREADY_EXISTS_MESSAGE

    else:
        new_student = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(new_student)
        return "is added."


def update_student(name):
    """
    Update an existing student record.
    Returns error if student is not found, updated name already exists or updated values are no valid.
    :param name: The name of the student whose record is to be updated.
    :return: (str) The result of the update
    """
    for current_student in students:

        if current_student["name"] == name:
            # Student is found. Prompt the user to enter the updated fields and validate each input.
            # Keep current values if fields are empty
            print("Enter updated name (leave empty to skip):", end=" ")
            updated_name_candidate = input()
            updated_name_candidate = validate_student_name(updated_name_candidate, "update")
            updated_candidate_index = students.index(current_student)

            if updated_name_candidate:
                # If the name is to be updated, verify that the new value does not already exists for other student
                # since our identification is done by name
                for existing_student in students:

                    if existing_student["name"] == updated_name_candidate \
                            and students.index(existing_student) != updated_candidate_index:

                        return STUDENT_ALREADY_EXISTS_MESSAGE

                else:
                    updated_name = updated_name_candidate

            else:   # updated name is empty (i.e. unchanged)
                updated_name = updated_name_candidate

            print("Enter updated age (leave empty to skip):", end=" ")
            input_age = input()
            updated_age, message = validate_student_age(input_age)

            if updated_age == INVALID_AGE_VALUE:
                return message

            print("Enter updated grade (leave empty to skip):", end=" ")
            input_grade = input()
            updated_grade, message = validate_student_grade(input_grade)

            if updated_grade == INVALID_GRADE_VALUE:
                return INVALID_GRADE_VALUE_MESSAGE

            print("Enter student's subjects (comma-separated or leave empty to skip):", end=" ")
            subjects_input = input()
            updated_subjects = format_student_subjects(subjects_input)

            # Prompted values were validated.
            # Do actual update on student:
            if updated_name:
                current_student["name"] = updated_name
            if updated_age:
                current_student["age"] = updated_age
            if updated_grade:
                current_student["grade"] = updated_grade
            if updated_subjects:
                del current_student["subjects"]
                current_student["subjects"] = updated_subjects

            return "Student was updated."

    else:
        return STUDENT_NOT_FOUND


def delete_student(name):
    """
    Delete a student record based on the student's name. If student is not found, returns error message.
    :param name: The name of the student to delete.
    :return: (str) Result of the deletion.
    """
    for current_student in range(len(students)):

        if name == students[current_student]["name"]:
            del students[current_student]
            return f"Student {name} is deleted."

    else:
        return STUDENT_NOT_FOUND


def search_student(name):
    """
    Search for a student by name and return their record.
    :param name: The name of the student to search for.
    :return: (str) Formatted student information.
    """

    student_information = ""
    for current_student in range(len(students)):

        if name == students[current_student]["name"]:

            student_information = f'\nStudent name: {students[current_student]["name"]}'

            if students[current_student]["age"]:
                student_information += f'\nStudent age: {students[current_student]["age"]}'
            else:
                student_information += f'\nStudent age: (undefined)'

            if students[current_student]["grade"]:
                student_information += f'\nStudent grade: {students[current_student]["grade"]:.2f}'
            else:
                student_information += f'\nStudent age: (undefined)'

            student_information += "\nSubjects: "

            for student_subject in students[current_student]["subjects"]:
                student_information += f'\n\tSubject: {student_subject}'

            return student_information

    else:
        return STUDENT_NOT_FOUND


def list_all_students():
    """
    List all student records.
    """
    students_count = len(students)

    if students_count > 0:

        for current_student in range(students_count):

            student_information = f'\nStudent name: {students[current_student]["name"]}'

            if students[current_student]["age"]:
                student_information += f'\nStudent age: {students[current_student]["age"]}'
            else:
                student_information += f'\nStudent age: (undefined)'

            if students[current_student]["grade"]:
                student_information += f'\nStudent grade: {students[current_student]["grade"]:.2f}'
            else:
                student_information += f'\nStudent age: (undefined)'

            student_information += "\nSubjects: "

            for student_subject in students[current_student]["subjects"]:
                student_information += f'\n\tSubject: {student_subject}'

            print(student_information)

        print(f"\nListed {students_count} students.")

    else:
        print(f"\nThere are no students to be listed.")


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':

            print("Enter student's name: ", end=" ")
            input_name = input()
            student_name = validate_student_name(input_name, "add")

            if student_name == INVALID_NAME_VALUE:
                print(INVALID_NAME_VALUE)
                continue

            print("Enter student's age: ", end=" ")
            input_age = input()
            student_age, message = validate_student_age(input_age)

            if student_age == INVALID_AGE_VALUE:
                print(message)
                continue

            print("Enter student's grade: ", end=" ")
            input_grade = input()
            student_grade, message = validate_student_grade(input_grade)

            if student_grade == INVALID_GRADE_VALUE:
                print(INVALID_GRADE_VALUE_MESSAGE)
                continue

            print("Enter student's subjects (comma-separated): ", end=" ")
            input_subjects = input()
            student_subjects = format_student_subjects(input_subjects)

            # Input was validated. Add the student.
            message = add_student(student_name, student_age, student_grade, student_subjects)
            print(f"{student_name} {message}")

        elif choice == '2':

            print("Enter student's name to update: ", end=" ")
            # Prompt the user to enter name of the student which will be updated and validate the name is not empty.
            student_name = input()
            student_name = validate_student_name(student_name, "search")

            if student_name == INVALID_NAME_VALUE:
                print(INVALID_NAME_VALUE)
                continue

            # Call the update_student function
            message = update_student(student_name)
            print(message)

        elif choice == '3':

            print("Enter student's name to delete: ", end=" ")
            # Prompt the user to enter name of the student to be searched and validate the name is not empty.
            student_name = input()
            student_name = validate_student_name(student_name, "delete")

            if student_name == INVALID_NAME_VALUE:
                print(INVALID_NAME_VALUE)
                continue

            # Call the delete_student function
            message = delete_student(student_name)
            print(message)

        elif choice == '4':

            print("Enter student's name to search: ", end=" ")
            # Prompt the user to enter name of the student to be searched and validate the name is not empty.
            student_name = input()
            student_name = validate_student_name(student_name, "search")

            if student_name == INVALID_NAME_VALUE:
                print(INVALID_NAME_VALUE)
                continue

            # Call the search_student function
            message = search_student(student_name)
            print(message)

        elif choice == '5':

            # Call the list_all_students function
            list_all_students()

        elif choice == '6':

            # Exit the program
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
