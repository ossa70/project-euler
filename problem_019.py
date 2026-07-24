# Counting Sundays
import datetime

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)

counter = 0

year, month = start.year, start.month
while (year, month) <= (end.year, end.month):
    if datetime.date(year, month, 1).weekday() == 6:
        counter += 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(counter)

# Manual version, without datetime, for comparison/understanding

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    lengths = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return lengths[month - 1]

# Given fact: 1 Jan 1900 was a Monday (Monday=0, ..., Sunday=6)
day_of_week = 0
manual_counter = 0

for year in range(1900, 2001):
    for month in range(1, 13):
        if year >= 1901 and day_of_week == 6:
            manual_counter += 1
        day_of_week = (day_of_week + days_in_month(year, month)) % 7

print(manual_counter)