# Code by abhis021@github

# Take day input and check if it's within the valid range
day = int(input("Input a day [1-31]: "))
if day < 1 or day > 31:  # Day must be between 1 and 31
    print("Invalid day, exiting...")
    exit()

# Take month input and check if it's within the valid range
month = int(input("Input a month [1-12]: "))
if month < 1 or month > 12:  # Month must be between 1 and 12
    print("Invalid month, exiting...")
    exit()

# Take year input and check if it's within the valid range
year = int(input("Input a year [1900-2025]: "))
if year < 1900 or year > 2099:  # Year must be between 1900 and 2099
    print("Invalid year, exiting...")
    exit()

# Check if the entered year is a leap year
# Leap year conditions:
# - Divisible by 400, or
# - Divisible by 4 but not by 100
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# Determine the number of days in the given month
if month in (1, 3, 5, 7, 8, 10, 12):  # Months with 31 days
    month_length = 31
elif month == 2:  # February has 28 or 29 days depending on leap year status
    month_length = 29 if leap_year else 28
else:  # All other months (April, June, September, November) have 30 days
    month_length = 30

# Calculate the next day
if day < month_length:  # If it’s not the last day of the month, just add 1
    day += 1
else:  # If it’s the last day of the month
    day = 1  # Reset day to 1
    if month == 12:  # If it’s December, reset month to January and increment year
        month = 1
        year += 1
    else:  # Otherwise, move to the next month
        month += 1

# Print the result in dd-mm-yyyy format with zero-padded day and month
print(f"The next date is [dd-mm-yyyy] {day:02d}-{month:02d}-{year}.")
