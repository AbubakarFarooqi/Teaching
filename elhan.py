def Factorial_using_while(input_num):
    num=1
    factorial=1
    while num <= input_num:
        factorial=factorial*num
        num=num+1
    print(f"The factorial of {input_num} is {factorial}")

def Factorial_using_for(input_num):
    factorial=1
    for i in range(1,input_num+1):
        factorial=factorial*i
    print(f"The factorial of {input_num} is {factorial}")

def main():
    num=int(input("Type in a number-> "))
    Factorial_using_for(num)
    Factorial_using_while(num)
    
if __name__ == "__main__":
    main()