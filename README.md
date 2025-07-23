# 📊 Group 1 – Big Data Analytics: Class Quiz I
### 📚 Course: INSY 8413 – *Introduction to Big Data Analytics*  
### 🏫 Institution: Adventist University of Central Africa (AUCA)  
### 👨‍🏫 Instructor: Eric Maniraguha  
### 🗓️ Semester: Academic Year 2024–2025, SEM II  
### 👥 Group: Group 1 (Grp 

---

## 🧾 Introduction

This repository contains our group’s solution for **Class Quiz I**, covering Python fundamentals in the context of data analytics.  
The tasks demonstrate our practical understanding of:

- Writing reusable Python functions
- Manipulating strings and text inputs
- Building interactive logic with user inputs in **Jupyter Notebook**

Each problem was tackled collaboratively to reflect both individual and team learning outcomes.

---

## 📁 Quiz Contents

### ✅ Task 1: Age calculator using a Function
> Calculates and displays the user's age based on input and the current year (2025).

### ✅ Task 2: Palindrome Checker
> Validates whether a given string reads the same forwards and backwards.

### ✅ Task 3: Iterating Over Two Text Inputs
> Combines two text inputs and returns a list of characters from the combined string.

---

## 🧑‍💻 Group Members

| Student ID | Full Name          |
|------------|--------------------|
| 26661   | Ishimwe Egîdë      |
| 24810  | Kaliza Natasha Peace |
| 25618   | Ishimwe Divin Elvis  |
| 26594   | Akanyana Lesly    |
| 27020 | Nshimyumuremyi Elias    |
| 25815   | Munezero Irakoze Luccin |

> ℹ️ 

---
![WhatsApp Image 2025-06-26 at 11 21 52_d3203886](https://github.com/user-attachments/assets/1df1bfe8-0771-446e-b35a-3cfac02a642a)

## 🧠 Task Documentation

### 🧮 Question 1: Age Calculator using a Function

#### 📌 Objective
Build a function that calculates a user’s age based on the current year (`2025`) and their input birth year.

## 💻 Code
```python
def calculate_age(birth_year):
    current_year = 2025
    return current_year - birth_year

def get_user_input():
    print("🎉 Welcome to the Age Calculator! 🎉")
    while True:
        name = input("📝 Enter your name: ").strip()
        if not name.isalpha():
            print("❌ Name must contain letters only.")
        else:
            break

    while True:
        year_input = input("📅 Enter your year of birth: ").strip()
        if not year_input.isdigit():
            print("❌ Please enter a number.")
            continue

        birth_year = int(year_input)
        if birth_year < 1900 or birth_year > 2025:
            print("⚠️ Enter a year between 1900 and 2025.")
        else:
            break

    return name, birth_year

name, birth_year = get_user_input()
age = calculate_age(birth_year)
print("\n✅ Thank you,", name + "!")
print("🎂 You are", age, "years old.")
```

### 🖥️ Output Example
```plaintext

🎉 Welcome to the Age Calculator! 🎉
📝 Enter your name: Ishimwe
📅 Enter your year of birth: 2020

✅ Thank you, Ishimwe!
🎂 You are 5 years old.
```

# 📸 Screenshot
![python q1](https://github.com/user-attachments/assets/23d32a37-8019-403d-aa2f-99b11060a944)

## 🔄 Question 2: Palindrome Checker

### 📌 Objective

Build a program that checks if the input word or sentence is a palindrome — reads the same forward and backward.

### 💻 Code
```python

import re

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def get_valid_input():
    print("\n🔄 Palindrome Checker 🔄")
    while True:
        user_input = input("✏️ Enter a word or sentence: ").strip()

        if not user_input:
            print("⚠️ Cannot be empty.")
            continue
        if len(user_input.replace(" ", "")) < 2:
            print("⚠️ At least two characters required.")
            continue
        if user_input.isnumeric():
            print("🚫 Numbers only are not allowed.")
            continue
        if not re.match(r'^[A-Za-z ]+$', user_input):
            print("🚫 Use only letters and spaces.")
            continue

        return user_input

text = get_valid_input()
if is_palindrome(text):
    print("✅ This is a palindrome!")
else:
    print("❌ This is NOT a palindrome.")
```
### 🖥️ Output Example
```plaintext
✏️ Enter a word or sentence: A man a plan a canal Panama
✅ This is a palindrome!
```
# 📸 Screenshot 
![python q2](https://github.com/user-attachments/assets/50c45ffe-9ead-438d-9bbb-8b206879d553)

## 🔤 Question 3: Character Iterator from Two Texts

### 📌 Objective

Take two text inputs, combine them, and display a list of characters from the merged string.

## 💻 Code

```python

def get_text_input(prompt):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("⚠️ Input cannot be empty.")
            continue
        if user_input.isspace():
            print("⚠️ Input cannot be only spaces.")
            continue
        if user_input.isdigit():
            print("🚫 Numbers only are not allowed.")
            continue

        return user_input

print("\n🔡 Character Iterator 🔡")
text1 = get_text_input("✏️ Enter the first text: ")
text2 = get_text_input("✏️ Enter the second text: ")

combined_text = text1 + text2
character_list = list(combined_text)

print("\n✅ Combined Text:", combined_text)
print("📃 List of characters:")
print(character_list)
```
## 🖥️ Output Example

```plaintext
✏️ Enter the first text: Hello
✏️ Enter the second text: World

✅ Combined Text: HelloWorld
📃 List of characters:
['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

```
📸 Screenshot


![python q3](https://github.com/user-attachments/assets/6c7d9fac-31bf-45ad-9b8e-d02c97d1f972)




