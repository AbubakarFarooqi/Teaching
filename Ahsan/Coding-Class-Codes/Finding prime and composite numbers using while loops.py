num=int(input("Enter a number here -> "))
i=2
prime=True

while i<=num-1:
    if num % 2 == 0:
        prime=False
        break
    i=i+1

if prime==True:
    print (f"{num} is prime.")
else:
         print (f"{num} is not prime.")
