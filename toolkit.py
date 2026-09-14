# Personal Mini-Toolkit
# This program provides several simple tools through a menu.

print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")

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
        print("To-Do List selected.")

    elif choice == "3":
        print("Number Guessing Game selected.")

    elif choice == "4":
        print("Thanks for using my Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
