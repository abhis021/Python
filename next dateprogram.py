# Code by abhis021@github
day = int(input("Input a day [1-31]: "))
if day < 1 or day > 31:
    print("Invalid day, exiting...")
    exit()

month = int(input("Input a month [1-12]: "))
if month < 1 or month > 12:
    print("Invalid month, exiting...")
    exit()

year = int(input("Input a year [1900-2025]: "))
if year < 1900 or year > 2025:
    print("Invalid year, exiting...")
    exit()

# Check if it's a leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# Determine the number of days in the month
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    month_length = 29 if leap_year else 28
else:
    month_length = 30

# Calculate the next day
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

# Print the result in dd-mm-yyyy format
print(f"The next date is [dd-mm-yyyy] {day:02d}-{month:02d}-{year}.")
