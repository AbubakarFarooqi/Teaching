a = int(input("Enter a number: "))
try:
    result = 10 / a
except ZeroDivisionError:
    print("You can't divide by zero!")