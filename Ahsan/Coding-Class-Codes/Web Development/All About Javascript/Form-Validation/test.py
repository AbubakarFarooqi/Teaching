n = int(input("Enter a number-> "))

isPrime = True # Flags/decision/variable

for i in range (2,n):
    if n % i == 0:
        isPrime = False

if isPrime == True:
    print(n, " is a prime number!")
else:
    print(n, " is not a prime number!")
