# List of dictionaries to store all students
students = list()


def prompt_and_validate_student_name(operation):
    """
    Prompts for a student name.
    If the function is called for update of an existing student, empty value is accepted.
    If the function is called to add, delete or search for a student, the user is prompted to try again.
    Args:
    - operation (str): Operation from which the prompt was called - add, update, delete, search.
    :return: str(name)
    """
    name = input().strip()
    if name == "" and (operation == "add" or operation == "delete" or operation == "search"):
        print(f"Enter a valid student name. Name cannot be empty. Please try again.")
        return
    else:
        return name


def prompt_and_validate_student_age():
    """
    Prompts for student age.
    If age is not a positive integer number, input is not validated and the user is prompted to try again.
    :return: int(age)
    """
    age_input = input()
    if age_input == "":
        return
    else:
        try:
            age = int(age_input)
        except ValueError:
            print(f"The age you entered is invalid. Please try again. ")
            return -1
        else:
            if age <= 0:
                print(f"Student age must be a positive value. Please try again. ")
                return -1
            else:
                return age


def prompt_and_validate_student_grade():
    """
    Prompts for student grade.
    A valid student grade is a float number between 2.00 and 6.00.
    :return: float(grade)
    """
    student_grade_input = input()
    if student_grade_input == "":
        return
    else:
        try:
            grade = float(student_grade_input)
        except ValueError:
            print(f"Invalid student grade. Grade must be a value between [2.00, 6.00]: ")
            return -1
        else:
            if grade < 2.00 or grade > 6.00:
                print(f"Invalid student grade. Grade must be a value between [2.00, 6.00]. Please try again. ")
                return -1
            else:
                return grade


def prompt_student_subjects():
    """
    Prompts for student subjects.
    :return: list(subjects)
    """
    subjects = input()
    if subjects == "":
        listed_subjects = list()
    else:
        listed_subjects = subjects.split(',')
        # remove spaces before and after subjects in list
        for subject_index in range(len(listed_subjects)):
            listed_subjects[subject_index] = str(listed_subjects[subject_index]).strip()

    return listed_subjects


def add_student(name, age, grade, subjects):
    """
    Add a new student record. Each student is a dictionary with keys: name, age, grade, and subjects.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    for current_student in students:
        if current_student["name"] == name:
            print(f"Student {name} already exists.")
            break
    else:
        new_student = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(new_student)
        print(f"Student {name} added.")


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """

    for current_student in students:

        if current_student["name"] == name:
            # Student is found. Prompt the user to enter the updated fields and validate each input.
            # Keep current values if fields are empty
            print("Enter updated name (leave empty to skip):", end=" ")
            updated_name_candidate = prompt_and_validate_student_name("update")
            updated_candidate_index = students.index(current_student)

            if updated_name_candidate:
                # If the name is to be updated, verify that the new value does not already exists for other student
                # since our identification is done by name
                for existing_student in students:
                    if existing_student["name"] == updated_name_candidate \
                            and students.index(existing_student) != updated_candidate_index:
                        print("Student with this name already exists. Please try again.")
                        return
                else:
                    # Student can be updated to the new name. There is no conflict with other students.
                    # Current student name is accepted.
                    updated_name = updated_name_candidate
            else:   # updated name is empty (i.e. unchanged)
                updated_name = updated_name_candidate

            print("Enter updated age (leave empty to skip):", end=" ")
            updated_age = prompt_and_validate_student_age()
            if updated_age == -1:
                print("Invalid updated age value. Please try again. ")
                break

            print("Enter updated grade (leave empty to skip):", end=" ")
            updated_grade = prompt_and_validate_student_grade()
            if updated_grade == -1:
                print("Invalid upgrade grade value. Please try again. ")
                break

            print("Enter student's subjects (comma-separated or leave empty to skip):", end=" ")
            updated_subjects = prompt_student_subjects()

            # Prompted values were validated. Do actual update on student:
            if updated_name:
                current_student["name"] = updated_name
            if updated_age:
                current_student["age"] = updated_age
            if updated_grade:
                current_student["grade"] = updated_grade
            if updated_subjects:
                del current_student["subjects"]
                current_student["subjects"] = updated_subjects

            print("Student was updated.")
            break
    else:
        print("Student is not found. Update is allowed on existing students only. Please try again. ")


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    for current_student in range(len(students)):
        if name == students[current_student]["name"]:
            print("Student exists. Deleting it...")
            del students[current_student]
            break
    else:
        print(f"Student {name} not found. Student must exists to delete it.")


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    for current_student in range(len(students)):
        if name == students[current_student]["name"]:
            print(f'\nStudent name: {students[current_student]["name"]}')
            if students[current_student]["age"]:
                print(f'Student age: {students[current_student]["age"]}')
            else:
                print(f"Student age: (undefined)")
            if students[current_student]["grade"]:
                print(f'Student grade: {students[current_student]["grade"]:.2f}')
            else:
                print(f"Student age: (undefined)")
            for student_subject in students[current_student]["subjects"]:
                print(f"\tSubject: {student_subject}")
            break
    else:
        print(f"Student {name} is not found.")


def list_all_students():
    """
    List all student records.
    """
    students_count = len(students)
    if students_count > 0:
        for current_student in range(students_count):
            print(f'\nStudent name: {students[current_student]["name"]}')
            if students[current_student]["age"]:
                print(f'Student age: {students[current_student]["age"]}')
            else:
                print(f"Student age: (undefined)")
            if students[current_student]["grade"]:
                print(f'Student grade: {students[current_student]["grade"]:.2f}')
            else:
                print(f"Student age: (undefined)")
            if students[current_student]["subjects"]:
                print(f"Subjects:")
                for student_subject in students[current_student]["subjects"]:
                    print(f"\tSubject: {student_subject}")
            else:
                print(f"Subjects: (undefined)")

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

        if choice == '1':  # Add Student

            print("Enter student's name: ", end=" ")
            name = prompt_and_validate_student_name("add")
            if not name:
                continue

            print("Enter student's age: ", end=" ")
            age = prompt_and_validate_student_age()
            if age == -1:
                continue

            print("Enter student's grade: ", end=" ")
            grade = prompt_and_validate_student_grade()
            if grade == -1:
                continue

            print("Enter student's subjects (comma-separated): ", end=" ")
            subjects = prompt_student_subjects()

            # Input was validated. Add the student.
            add_student(name, age, grade, subjects)

        elif choice == '2':

            print("Enter student's name to update: ", end=" ")
            # Prompt the user to enter name of the student which will be updated and validate the name is not empty.
            name = prompt_and_validate_student_name("search")
            if not name:
                continue

            # Call the update_student function
            update_student(name)

        elif choice == '3':

            print("Enter student's name to delete: ", end=" ")
            # Prompt the user to enter name of the student to be searched and validate the name is not empty.
            name = prompt_and_validate_student_name("delete")
            if not name:
                continue

            # Call the delete_student function
            delete_student(name)

        elif choice == '4':

            print("Enter student's name to search: ", end=" ")
            # Prompt the user to enter name of the student to be searched and validate the name is not empty.
            name = prompt_and_validate_student_name("search")
            if not name:
                continue

            # Call the search_student function
            search_student(name)

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