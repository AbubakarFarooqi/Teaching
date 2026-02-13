def sum(x,y):
    result=x+y
    return result
def diff(x,y):
    result=x-y
    return result
def product(x,y):
    result=x*y
    return result
def quotient(x,y):
    result=x/y
    return result

def main():
    num1=float(input("Enter first number-> "))
    num2=float(input("Enter second number-> "))
    operation=input("What is the operation?-> ")
    result=None
    if operation == "+":
        result=sum(num1,num2)
    elif operation == "-":
        result=diff(num1,num2)
    elif operation == "*":
        result=product(num1,num2)
    elif operation == "/":
        result=quotient(num1,num2)
    print(result)

if __name__ == "__main__":
    main()