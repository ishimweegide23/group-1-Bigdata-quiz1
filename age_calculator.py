def calculate_age(birth_year):
    current_year = 2025
    return current_year - birth_year

name = input("Enter your name: ")
year = int(input("Enter your birth year (e.g., 2000): "))
print(f"Hi {name}, your age is {calculate_age(year)}")
