num1 = int(input("Enter  number 1-> "))
num2 = int(input("Enter  number 2-> "))

divisor  = 0
dividend = 0

if num1 > num2:
    dividend = num1
    divisor  = num2
else:
    dividend = num2
    divisor  = num1
hcf = 0

while hcf == 0:
    rem = dividend % divisor

    if rem == 0:
        hcf = divisor

    if rem < divisor:
        dividend = divisor
        divisor = rem
    else:
        dividend = rem

print("HCF is ",hcf)