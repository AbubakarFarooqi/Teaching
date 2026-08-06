def add_numbers(num1,num2):
    sum = num1+num2
    return sum

def main():
    num1 = int(input("enter a number-> "))
    num2 = int(input("enter a number-> "))
    sum = add_numbers(num1,num2)
    print(f"Sum is {sum}")

if __name__ == "__main__": #entry point
    main()