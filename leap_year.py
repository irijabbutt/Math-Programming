# check if a given year is leap year or not
def is_leap_year(year):
 return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = 1000
print("Is", year, "a leap year?", is_leap_year(year))