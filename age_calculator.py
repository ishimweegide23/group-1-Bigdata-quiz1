def calculate_age(birth_year):
    current_year = 2025
    return current_year - birth_year

# Get user input
name = input("Enter your name: ")

while True:
    try:
        year_of_birth = int(input("Enter your year of birth (e.g., 2000): "))
        if 1900 <= year_of_birth <= 2025:
            break
        else:
            print("Please enter a valid year between 1900 and 2025.")
    except ValueError:
        print("Invalid input. Please enter a numeric year.")

# Calculate age
age = calculate_age(year_of_birth)

# Display result
print(f"Thank you\n{name}, your age is: {age}")
