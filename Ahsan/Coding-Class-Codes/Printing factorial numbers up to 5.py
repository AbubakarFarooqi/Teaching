num=int(input("Enter your number -> "))
f=1
i=1

while i<=num:
    f=i*f
    i=i+1

print (f"The factorial of {num} is {f}.")
