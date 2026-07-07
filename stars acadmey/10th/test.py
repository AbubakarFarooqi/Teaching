#write a program that input a number from user
# and check whether that number is even or odd
num1 = int(input("Enter a number 1 -> "))
num2 = int(input("Enter a number 2 -> "))

dividend = 0
divisor = 0

if num1 < num2:
    dividend = num2
    divisor = num1
else:
    divisor = num2
    dividend = num1

hcf = 0

while hcf == 0:
    rem = dividend % divisor # rem = 0 divisor = 9
    if rem == 0:
        hcf = divisor # hcf = 9

    if rem < divisor:
        dividend = divisor # dividend = 9
        divisor = rem # divisor = 0
    else: 
        dividend = rem

    
print(f"HCF is {hcf}")