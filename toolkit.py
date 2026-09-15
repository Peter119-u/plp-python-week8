# Personal Mini-Toolkit
# This program provides several simple tools through a menu.

print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")
print("Choose a tool and have fun!\n")


while True:
    print("\nPlease choose a tool:")
    print("1. Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        # Calculator: performs basic arithmetic on two numbers.
        print("\n--- Calculator ---")

        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                continue
            result = num1 / num2
        else:
            print(f"Sorry, '{operator}' is not a valid operation.")
            continue

        print(f"Your answer is: {result}")

    elif choice == "2":
        # To-Do List: lets the user add and view tasks stored in a list.
        print("\n--- To-Do List ---")

        tasks = []

        while True:
            print("\n1. Add a task")
            print("2. View tasks")
            print("3. Return to main menu")

            todo_choice = input("Choose an option: ")

            if todo_choice == "1":
                task = input("Enter a task: ")
                tasks.append(task)
                print(f"Task added: {task}")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, '{todo_choice}' is not a valid option.")

    elif choice == "3":
        # Number Guessing Game: keeps asking until the player guesses correctly.
        print("\n--- Number Guessing Game ---")

        secret_number = 7
        attempts = 0

        print("I am thinking of a number between 1 and 10.")

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break

    elif choice == "4":
        print("\nThanks for using my Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")