# Take a number and check:

# Even or Odd

num = int(input("Enter a number: "))
if num % 2 ==0:
    print("Even")
else:
    print("Odd")

#     Print numbers from 1 to 50:

# Only even numbers

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

# Take a number and:

# Print multiplication table

num = int(input("\nEnter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Find:

# Sum of numbers from 1 to N

N = int(input("Enter a number: "))
total_sum = sum(range(1, N + 1))
print(f"Sum of numbers from 1 to {N} is: {total_sum}")  


# Project: Simple Calculator
# Features:
# Take two numbers
# Take operation (+, -, *, /)
# Print result

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"
print(f"Result: {result}")

# Take a number and print:

# Positive / Negative / Zero

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Take two numbers and print:

# Largest number

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal")


# Check if a number is divisible by:

# 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")


# Print numbers from 1 to N

N = int(input("Enter a number: "))
print(f"Numbers from 1 to {N}:")
for i in range(1, N + 1):
    print(i, end=" ")

# Print:

# Sum of first N numbers

N = int(input("Enter a number: "))
total_sum = sum(range(1, N + 1))
print(f"Sum of first {N} numbers is: {total_sum}")

# Print:

# Multiplication table of a number

num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Reverse a number
# 👉 Example: 123 → 321

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Reversed number: {reversed_num}")   


# Count digits in a number
# 👉 Example: 12345 → 5

num = int(input("Enter a number: "))
digit_count = 0
while num > 0:
    num //= 10
    digit_count += 1
print(f"Number of digits: {digit_count}")

# Check if a number is:

# Palindrome (121 → Yes)

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome")
else:
    print(f"{original_num} is not a palindrome")

# Print all even numbers from 1 to 100

print("Even numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")

# Print all odd numbers from 1 to 100

print("\nOdd numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")

# Find:

# Sum of even numbers from 1 to N

N = int(input("Enter a number: "))
even_sum = sum(i for i in range(1, N + 1) if i % 2 == 0)
print(f"Sum of even numbers from 1 to {N} is: {even_sum}")



# Find:

# Factorial of a number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")

# Check if a number is:

# Prime

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

else:
    print(f"{num} is not a prime number")   



# Print Fibonacci series up to N terms

N = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b

# Find:

# Largest digit in a number

num = int(input("Enter a number: "))
largest_digit = 0
while num > 0:
    digit = num % 10
    if digit > largest_digit:
        largest_digit = digit
    num //= 10
print(f"Largest digit: {largest_digit}")


# Find:

# Sum of digits of a number

num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
print(f"Sum of digits: {digit_sum}")

# Check if a number is:

# Armstrong number
# 👉 Example: 153 → 1³ + 5³ + 3³ = 153

num = int(input("Enter a number: "))
original_num = num
armstrong_sum = 0
while num > 0:
    digit = num % 10
    armstrong_sum += digit ** 3
    num //= 10  
if original_num == armstrong_sum:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")


# Print pattern:

# *
# **
# ***
# ****

rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)

# Print pattern:
# ****
# ***   
# **
# *

rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)


# Take input until user enters 0
# 👉 Print sum of all numbers

total_sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num

print(f"Sum of all numbers: {total_sum}")


# Count vowels in a string


string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print(f"Number of vowels: {vowel_count}")


# Reverse a string
# 👉 "hello" → "olleh"

string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")


# Check if a string is palindrome

astring = input("Enter a string: ")
if astring == astring[::-1]:
    print(f"{astring} is a palindrome")
else:
    print(f"{astring} is not a palindrome")


# Find:

# Maximum number in a list

numbers = [3, 5, 1, 9, 2]
max_number = max(numbers)
print(f"Maximum number: {max_number}")

# Find:
# Minimum number in a list
numbers = [3, 5, 1, 9, 2]
min_number = min(numbers)
print(f"Minimum number: {min_number}")


# Remove duplicates from a list
numbers = [3, 5, 1, 9, 2, 5, 1]
unique_numbers = list(set(numbers))
print(f"List without duplicates: {unique_numbers}")

# Sort a list without using sort()

numbers = [3, 5, 1, 9, 2]
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

# Find second largest number in a list


numbers = [3, 5, 1, 9, 2]
unique_numbers = list(set(numbers))
unique_numbers.remove(max(unique_numbers))
print(f"Second largest number: {max(unique_numbers)}")


# Create a simple menu-driven calculator using loop

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"Result: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid choice, please try again.")



# 1. Number Guessing Game
# Task:
# Generate a random number (1–100)
# User keeps guessing
# Give hints:
# Too high / Too low
# Stop when correct
# Concepts:

# ✔ loops, conditions, random

import random 
number_to_guess = random.randint(1, 100)
while True:
    user_guess = int(input("Guess the number (1-100): "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break

    print("Game over. The number was:", number_to_guess)


# 2. Simple ATM System
# Features:
# Check balance
# Deposit
# Withdraw
# Exit
# Concepts:

# ✔ loops, if-else, input

balance = 1000.0
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Your balance is: ${balance:.2f}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"${amount:.2f} deposited. New balance: ${balance:.2f}")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${balance:.2f}")
        else:
            print("Insufficient funds.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

print("ATM system has been exited.")


# 3. To-Do List App (CLI)
# Features:
# Add task
# View tasks
# Delete task
# Concepts:

# ✔ lists, loops

tasks = []
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == '2':
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("To-Do List is empty.")
    elif choice == '3':
        if tasks:
            task_index = int(input("Enter task number to delete: "))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        else:
            print("To-Do List is empty.")
    elif choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")  

print("To-Do List App has been exited.")


# 4. Password Strength Checker
# Rules:
# Length ≥ 8
# Contains number
# Contains uppercase
# Output:
# Weak / Medium / Strong
# Concepts:

# ✔ strings, conditions

password = input("Enter a password: ")
strength = "Weak"
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            strength = "Strong"
        else:
            strength = "Medium"
    else:
        strength = "Medium"
print(f"Password strength: {strength}")


# 5. Quiz Game
# Features:
# Ask 5 questions
# Track score
# Show result
# Concepts:

# ✔ loops, variables

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "What is the highest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"}
]

score = 0
for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.strip().lower() == q["answer"].lower():
        score += 1

print(f"Your score is: {score}/{len(questions)}")

# 6. Contact Book
# Features:
# Add contact (name + number)
# Search contact
# Delete contact
# Concepts:

# ✔ dictionary


contacts = {}
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print("Contact added successfully.")
    elif choice == '2':
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"Contact found: {name} - {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == '4':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")


# 7. File Word Counter
# Task:
# Read a file
# Count:
# Words
# Lines
# Characters
# Concepts:

# ✔ file handling

file_path = input("Enter the file path: ")
try:
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        line_count = content.count('\n') + 1
        char_count = len(content)
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")
    print(f"Characters: {char_count}")
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")


# 8. Basic Login System
# Features:
# Username + password
# Allow 3 attempts
# Lock after failure
# Concepts:

# ✔ loops, conditions

correct_username = "admin"
correct_password = "password123"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. Attempts left: {attempts}")



# 9. Expense Tracker
# Features:
# Add expense
# Show total expense
# Show all entries
# Concepts:

# ✔ lists, loops

expenses = []
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Show Total Expense")
    print("3. Show All Entries")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        expenses.append({"amount": amount, "description": description})
    elif choice == '2':
        total_expense = sum(expense["amount"] for expense in expenses)
        print(f"Total expense: {total_expense}")
    elif choice == '3':
        for expense in expenses:
            print(f"Amount: {expense['amount']}, Description: {expense['description']}")
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break   

print("Expense Tracker has been exited.")

# 10. Multiplication Quiz Game
# Features:
# Ask random multiplication questions
# Track score
# Show result
# Concepts:

# ✔ loops, random, logic

score = 0
for _ in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    user_answer = int(input(f"What is {num1} x {num2}? "))
    if user_answer == correct_answer:
        score += 1

print(f"Your score is: {score}/5")



