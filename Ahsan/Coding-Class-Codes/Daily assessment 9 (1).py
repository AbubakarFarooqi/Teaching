num=int(input("Enter a number -> "))
i=2
prime=True

while i<=num-1:
    if num % i == 0:
        prime=False
    i=i+1

if prime==True:
    print (f"{num} is a prime number.")
else:
    prime=False
    print (f"{num} is not prime number.")
