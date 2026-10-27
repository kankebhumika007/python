# this program keeps asking the user to enter a number until they enter zero
num = int(input("Enter a number: "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number: "))

print("You entered zero. Program ended.")