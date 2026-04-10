# 1. Contact Book with File Storage
# Features:
# Add contact (name, number)
# Save to file
# Search contact
# Load contacts on start
# Concepts:

# ✔ dictionary + file handling

import json

contacts = {}
def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)
def add_contact(name, number):
    contacts[name] = number
    save_contacts()
def search_contact(name):
    return contacts.get(name, "Contact not found")
# Load contacts on start
load_contacts()
# Example usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print(search_contact("Alice"))  # Output: 123-456-7890
print(search_contact("Charlie"))  # Output: Contact not found



# 2. Password Manager (Basic)
# Features:
# Store website → password
# Save to file
# Retrieve password by site
# Concepts:

# ✔ dictionary + file read/write


passwords = {}
def load_passwords():
    global passwords
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}

def save_passwords():
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def add_password(site, username, password):
    passwords[site] = {"username": username, "password": password}
    save_passwords()

def get_password(site):
    return passwords.get(site, "Site not found")

# Load passwords on start
load_passwords()
# Example usage
add_password("example.com", "user1", "pass123")
add_password("test.com", "user2", "pass456")
print(get_password("example.com"))  # Output: {'username': 'user1', 'password': 'pass123'}
print(get_password("unknown.com"))  # Output: Site not found


# 3. Log Analyzer
# Input:

# Log file (text)

# Output:
# Count errors
# Count warnings
# Extract important lines
# Concepts:

# ✔ strings + file parsing


log_analyzer = {}
def analyze_log(file_path):
    global log_analyzer
    log_analyzer = {"errors": 0, "warnings": 0, "important_lines": []}
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if "ERROR" in line:
                    log_analyzer["errors"] += 1
                elif "WARNING" in line:
                    log_analyzer["warnings"] += 1
                if "IMPORTANT" in line:
                    log_analyzer["important_lines"].append(line.strip())
    except FileNotFoundError:
        print("Log file not found. Please check the path.")
    
    return log_analyzer

# Example usage
log_result = analyze_log('sample.log')
print(f"Errors: {log_result['errors']}")
print(f"Warnings: {log_result['warnings']}")
print("Important Lines:")
for line in log_result["important_lines"]:
    print(line)


# 4. Word Frequency Counter
# Features:
# Read file
# Count frequency of each word
# Display top frequent words
# Concepts:

# ✔ dictionary + string + file

def word_frequency(file_path):
    frequency = {}
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?";()')
                frequency[word] = frequency.get(word, 0) + 1
    return frequency    

# Example usage
freq_result = word_frequency(r"C:/Users/MI/Desktop/Python.txt")
sorted_freq = sorted(freq_result.items(), key=lambda x: x[1], reverse=True)
print("Top 5 Frequent Words:")
for word, count in sorted_freq[:5]:
    print(f"{word}: {count}")



# 5. Email Validator Tool
# Features:
# Input email
# Validate format
# Store valid emails in file
# Concepts:

# ✔ string validation + file

def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

def save_email(email):
    with open('valid_emails.txt', 'a') as f:
        f.write(email + '\n')

# Example usage
email = "TqG6H@example.com"
if validate_email(email):
    print("Valid email")
    save_email(email)
else:
    print("Invalid email")



#     6. Notes Manager (CLI)
# Features:
# Add note
# View notes
# Delete note
# Save notes in file
# Concepts:

# ✔ file handling + lists + strings

notes = []
def load_notes():
    global notes
    try:
        with open('notes.txt', 'r') as f:
            notes = f.read().splitlines()
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.txt', 'w') as f:
        f.write('\n'.join(notes))
def add_note(note):
    notes.append(note)
    save_notes()

def view_notes():
    return notes

def delete_note(index):
    if 0 <= index < len(notes):
        del notes[index]
        save_notes()
    else:
        print("Invalid index")


# Load notes on start
load_notes()
# Example usage
add_note("Buy groceries")
add_note("Call Alice")
print(view_notes())  # Output: ['Buy groceries', 'Call Alice']      
delete_note(0)
print(view_notes())  # Output: ['Call Alice']


# 7. Student Record System (File-Based)
# Features:
# Add student (name, marks)
# Save to file
# Calculate average
# Display topper
# Concepts:

# ✔ dictionary + file handling

students = {}
def load_students():
    global students
    try:
        with open('students.json', 'r') as f:
            students = json.load(f)
    except FileNotFoundError:
        students = {}

def save_students():
    with open('students.json', 'w') as f:
        json.dump(students, f)

def add_student(name, marks):
    students[name] = marks
    save_students()

def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def display_topper():
    if not students:
        return "No students found"
    topper = max(students, key=lambda x: calculate_average(students[x]))
    return topper, calculate_average(students[topper])

# Load students on start
load_students()
# Example usage
add_student("Alice", [85, 90, 78])
add_student("Bob", [92, 88, 95])
print(display_topper())  # Output: ('Bob', 91.66666666666667)


# 8. Username Generator
# Input:

# Full name

# Output:
# Generate username (e.g., roshni_patil_27)
# Concepts:

# ✔ string manipulation

def generate_username(full_name):
    name_parts = full_name.lower().split()
    username = "_".join(name_parts)
    return username

# Example usage
full_name = "Roshni Patil"
username = generate_username(full_name)
print(username)  # Output: roshni_patil


# 9. Text Formatter Tool
# Features:
# Convert text:
# Uppercase
# Lowercase
# Remove extra spaces
# Save formatted text to file
# Concepts:

# ✔ string operations + file

def format_text(text, option):
    if option == "uppercase":
        return text.upper()
    elif option == "lowercase":
        return text.lower()
    elif option == "remove_spaces":
        return " ".join(text.split())
    else:
        return text
    
def save_formatted_text(formatted_text):
    with open('formatted_text.txt', 'w') as f:
        f.write(formatted_text)


# Example usage
input_text = "  Hello   World!  "
formatted = format_text(input_text, "remove_spaces")
print(formatted)  # Output: "Hello World!"
save_formatted_text(formatted)


# 10. JSON-like Data Manager (Advanced Beginner)
# Features:
# Store data like:
# {
#   "name": "Roshni",
#   "skills": ["Python", "React"]
# }
# Save to file
# Read and display
# Concepts:

# ✔ dictionary + file + structured data

data_manager = {}
def load_data():
    global data_manager
    try:
        with open('data.json', 'r') as f:
            data_manager = json.load(f)
    except FileNotFoundError:
        data_manager = {}

def save_data():
    with open('data.json', 'w') as f:
        json.dump(data_manager, f)
def add_data(name, skills):
    data_manager[name] = skills
    save_data()

def display_data():
    return data_manager
# Load data on start
load_data()

# Example usage
add_data("Roshni", ["Python", "React"])
print(display_data())  # Output: {'Roshni': ['Python', 'React']}
