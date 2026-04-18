def prime_of_number (num):

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

for a in range (1,51):
    prime_of_number (a)

