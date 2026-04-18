# Write a function that will get a number as a parameter
# and starts a loop from 1 to that number and prints all
# the numbers that are divisible by 3 AND 5


def num(parameter):
    for a in range (1,parameter):
        a=a+1
        if a % 3 == 0 and a % 5 == 0:
            print (f"{a}")

parameter=int(input("Enter a number -> "))

num(parameter)


