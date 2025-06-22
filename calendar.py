
import calendar

# Get user input for year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

# Display the calendar for the given month and year
print(calendar.month(year, month))