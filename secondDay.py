# Write a function to:

# Check even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))

# Function to:

# Find largest of 3 numbers

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(find_largest(5, 10, 3))

# Function to:

# Calculate factorial

def calculate_factorial(n): 
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5))

# Function to:
# Check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))


# Find largest number in list

def find_largest_in_list(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(find_largest_in_list([3, 5, 7, 2, 8]))

# Find sum of all elements in list

def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print(sum_of_list([1, 2, 3, 4, 5]))

# Remove duplicates from list

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))

# Reverse a list

def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))

# Given a list:

# [10, 20, 30, 40]

# 👉 Create a function to:

# Return average

def calculate_average(lst):
    if not lst:
        return 0
    total = sum(lst)
    average = total / len(lst)
    return average

print(calculate_average([10, 20, 30, 40]))

# 👉 Given list:

# [1, 2, 2, 3, 4, 4]
# Return unique values

def unique_values(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(unique_values([1, 2, 2, 3, 4, 4]))


# Write a function to:

# Return square of a number

def square(num):
    return num ** 2

print(square(5))


# Write a function to:

# Check if a number is positive, negative, or zero

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))

# Function to:

# Find maximum of 3 numbers

def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(find_maximum(5, 10, 3))

# Function to:

# Return sum of digits of a number

def sum_of_digits(num):
    digit_sum = 0
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return digit_sum

print(sum_of_digits(1234))


# Function to:

# Reverse a number

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

print(reverse_number(1234))



# Function to:

# Count digits in a number

def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

print(count_digits(12343546789087654))


# Function to:

# Check if number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))



# Function to:

# Return factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# Function to:

# Return Fibonacci series up to N

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci_series(10))

# Function to:
# Return even numbers from 1 to N

def even_numbers(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(even_numbers(10))

# Function to:

# Find GCD of two numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))

# Function to:

# Convert Celsius → Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(25))


# Function to:

# Count vowels in a string

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World!"))

# Function to:

# Check if string is palindrome
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man a plan a canal Panama"))


# Find:

# Maximum element in list

lst = [3, 5, 7, 2, 8]
max_element = max(lst)

print(max_element)

# Find:

# Minimum element in list

min_element = min(lst)
print(min_element)


# Sum of all elements

total_sum = sum(lst)
print(total_sum)


# Average of list

average = total_sum / len(lst)
print(average)

# Count:

# Even and odd numbers in list

even_count = 0
odd_count = 0
for num in lst:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even count: {even_count}, Odd count: {odd_count}")


# Remove:

# Duplicates from list

ltist = [1, 2, 3, 2, 4, 1, 5, 5, 6, 7]
unique_list = list(set(ltist))
print(unique_list)  

# Reverse a list (without built-in function)


reversed_list = []
for i in range(len(ltist) - 1, -1, -1):
    reversed_list.append(ltist[i])
print(reversed_list)


# Sort a list (without using sort())


sorted_list = []
for num in ltist:
    inserted = False
    for i in range(len(sorted_list)):
        if num < sorted_list[i]:
            sorted_list.insert(i, num)
            inserted = True
            break
    if not inserted:
        sorted_list.append(num)
print(sorted_list)

# Find:

# Second largest number

def second_largest(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

print(second_largest([1, 2, 3, 4, 5]))


# Merge two lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print(merged_list)

# Find:

# Common elements in two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)

# Remove:

# All occurrences of a value

def remove_occurrences(lst, value):
    return [item for item in lst if item != value]

print(remove_occurrences([1, 2, 3, 2, 4, 1, 5], 2))


# Find:

# Frequency of each element

def frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


print(frequency([1, 2, 3, 2, 4, 1, 5]))

# Split list into:

# Even list and Odd list

def split_even_odd(lst):
    even_list = []
    odd_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list

print(split_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Rotate list:
# 👉 Example:

# [1, 2, 3, 4] → [2, 3, 4, 1]

def rotate_list(lst):
    if not lst:
        return lst
    first_element = lst[0]
    rotated_list = lst[1:] + [first_element]
    return rotated_list

print(rotate_list([1, 2, 3, 4]))


# Student Grade System
# Features:
# Input marks (list)
# Calculate:
# Total
# Average
# Assign grade:
# A, B, C, Fail
# Concepts:

# ✔ functions + lists + conditions

def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)
    
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    else:
        grade = 'Fail'
    
    return total, average, grade

marks = input("Enter marks separated by commas: ")

marks = list(map(int, marks.split(',')))
total, average, grade = calculate_grade(marks)
print(f"Total: {total}, Average: {average}, Grade: {grade}")


# 2. Number Statistics Analyzer
# Input:

# List of numbers

# Output:
# Max
# Min
# Average
# Count of even/odd
# Concepts:

# ✔ functions + loops

def analyze_numbers(numbers):
    if not numbers:
        return None
    
    max_num = max(numbers)
    min_num = min(numbers)
    average = sum(numbers) / len(numbers)
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    
    return max_num, min_num, average, even_count, odd_count

numbers = input("Enter numbers separated by commas: ")
numbers = list(map(int, numbers.split(',')))
max_num, min_num, average, even_count, odd_count = analyze_numbers(numbers)
print(f"Max: {max_num}, Min: {min_num}, Average: {average}, Even Count: {even_count}, Odd Count: {odd_count}")



# 3. List Search Tool
# Features:
# Search element in list
# Return index
# If not found → print message
# Concepts:

# ✔ functions + loops

def search_element(lst, element):
    for index, item in enumerate(lst):
        if item == element:
            return index
    return "Element not found"

my_list = input("Enter list elements separated by commas: ")
my_list = my_list.split(',')

element_to_search = input("Enter element to search: ")
result = search_element(my_list, element_to_search)
print(f"Element found at index: {result}" if isinstance(result, int) else result)


# 4. Duplicate Remover Tool
# Features:
# Take list
# Remove duplicates
# Return new list
# Concepts:

# ✔ list logic + functions

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = input("Enter list elements separated by commas: ")
my_list = my_list.split(',')
new_list = remove_duplicates(my_list)
print(f"List after removing duplicates: {new_list}")



# 5. Voting System
# Features:
# Candidates list
# Users vote
# Count votes
# Show winner
# Concepts:

# ✔ lists + counting logic


def voting_system(candidates, votes):
    vote_count = {candidate: 0 for candidate in candidates}
    
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
    
    winner = max(vote_count, key=vote_count.get)
    return winner, vote_count[winner]

candidates = input("Enter candidates separated by commas: ")
candidates = candidates.split(',')
votes = input("Enter votes separated by commas: ")
votes = votes.split(',')
winner, count = voting_system(candidates, votes)
print(f"Winner: {winner} with {count} votes")


# 6. Password Generator
# Features:
# Generate random password
# Include:
# letters
# numbers
# symbols
# Concepts:

# ✔ random + strings + logic

import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter desired password length: "))
password = generate_password(length)
print(f"Generated Password: {password}")


# 7. Shopping Cart System
# Features:
# Add items to cart
# Show cart
# Calculate total price
# Concepts:

# ✔ lists + functions

def add_to_cart(cart, item, price):
    cart.append((item, price))
    return cart

def show_cart(cart):
    if not cart:
        return "Cart is empty."
    return "\n".join(f"{item}: ${price}" for item, price in cart)

def calculate_total(cart):
    return sum(price for item, price in cart)

cart = []
while True:
    print("1. Add item to cart")
    print("2. Show cart")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart = add_to_cart(cart, item, price)
    elif choice == '2':
        print(show_cart(cart))
    elif choice == '3':
        total = calculate_total(cart)
        print(f"Total Price: ${total}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")


# 8. Marks Ranking System
# Features:
# Input marks list
# Sort marks
# Assign ranks
# Concepts:

# ✔ sorting logic + lists

def rank_marks(marks):
    sorted_marks = sorted(marks, reverse=True)
    ranks = {mark: rank + 1 for rank, mark in enumerate(sorted_marks)}
    return ranks

marks = input("Enter marks separated by commas: ")
marks = list(map(int, marks.split(',')))
ranks = rank_marks(marks)
for mark in marks:
    print(f"Mark: {mark}, Rank: {ranks[mark]}")



#     9. List Comparison Tool
# Features:
# Compare 2 lists
# Find:
# common elements
# unique elements
# Concepts:

# ✔ list operations


def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    unique_to_list1 = list(set(list1) - set(list2))
    unique_to_list2 = list(set(list2) - set(list1))
    
    return common_elements, unique_to_list1, unique_to_list2

list1 = input("Enter list 1 elements separated by commas: ")
list1 = list1.split(',')
list2 = input("Enter list 2 elements separated by commas: ")
list2 = list2.split(',')
common_elements, unique_to_list1, unique_to_list2 = compare_lists(list1, list2) 
print(f"Common Elements: {common_elements}")
print(f"Unique to List 1: {unique_to_list1}")
print(f"Unique to List 2: {unique_to_list2}")



# 10. Simple Library System
# Features:
# Add book
# Remove book
# Show available books
# Concepts:

# ✔ lists + functions


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book}' added to library."

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"Book '{book}' removed from library."
        else:
            return f"Book '{book}' not found in library."

    def show_books(self):
        if not self.books:
            return "No books available."
        return "Available Books:\n" + "\n".join(self.books)
    
library = Library()
while True:
    print("1. Add book")
    print("2. Remove book")
    print("3. Show available books")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        book = input("Enter book name: ")
        print(library.add_book(book))

    elif choice == '2':
        book = input("Enter book name: ")
        print(library.remove_book(book))

    elif choice == '3': 
        print(library.show_books())

    elif choice == '4':
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  

        
    

