#code by abhis021@github
# Program to calculate the day of the week for any given date
# using Zeller's Congruence formula.

def get_day_of_week(day, month, year):
    # If month is January or February, adjust month and year
    if month < 3:
        month += 12
        year -= 1

    # Zeller's Congruence formula
    k = year % 100          # Year of the century
    j = year // 100         # Zero-based century

    # Formula to calculate day of the week
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day_of_week = f % 7

    # Mapping numbers to day names
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

# Input from the user
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year (1-2999): "))

# Validate year range
if year < 1 or year > 2999:
    print("Invalid year. Please enter a year between 1 and 2999.")
else:
    # Get the day of the week
    day_name = get_day_of_week(day, month, year)
    print(f"The day of the week for {day}-{month}-{year} is {day_name}.")
