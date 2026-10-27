# this program checks if a year is a leap year or not
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")