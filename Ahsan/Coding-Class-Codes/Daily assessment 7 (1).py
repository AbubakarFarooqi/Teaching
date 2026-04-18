num=int(input("Enter a number -> "))
i=1
f=1
while i<=num:
    f=i*f
    i=i+1
print(f"The factorial of {num} is {f}.")
