# 📊 Group 1 – Big Data Analytics: Class Quiz I
### 📚 Course: INSY 8413 – *Introduction to Big Data Analytics*  
### 🏫 Institution: Adventist University of Central Africa (AUCA)  
### 👨‍🏫 Instructor: Eric Maniraguha  
### 🗓️ Semester: Academic Year 2024–2025, SEM II  
### 👥 Group: Group 1 (Grp A)

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
| 2561   | Ishimwe Divin Elvis  |
| 2659   | Akanyana Lesly    |
| 2702 | Nshimyumuremyi Elias    |
| 25815   | Munezero Irakoze Luccin |

> ℹ️ 

---

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

### 📸 Screenshot
![python q1](https://github.com/user-attachments/assets/23d32a37-8019-403d-aa2f-99b11060a944)
![python q1](https://github.com/user-attachments/assets/23d32a37-8019-403d-aa2f-99b11060a944)



