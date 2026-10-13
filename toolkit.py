
# Personal Mini-Toolkit
# This program contains a calculator, a to-do list, and an even-or-odd checker.


# TOOL 1: Simple Calculator
# This tool performs addition, subtraction, multiplication, and division.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    print(f"The answer is: {answer:g}")


# TOOL 2: To-Do List Manager
# This tool allows the user to add, view, and remove tasks.
def todo_list_manager():
    tasks = []

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added successfully: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(
                        input("Enter the number of the task to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task removed: {removed_task}")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


# TOOL 3: Even-or-Odd Checker
# This tool checks whether a whole number is even or odd.
def even_or_odd_checker():
    print("\n--- Even-or-Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


# MAIN MENU
# This menu keeps running until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Even-or-Odd Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()

        elif choice == "2":
            todo_list_manager()

        elif choice == "3":
            even_or_odd_checker()

        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break

        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please enter 1, 2, 3, or 4."
            )


# Start the program.
if __name__ == "__main__":
    main()