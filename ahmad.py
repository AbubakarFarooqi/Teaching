def multiple_of_10(num):
    if num % 10 == 0:
        print(f"{num} is divisible by 10")
    else:
        print(f"{num} isn't divisible by 10")

if __name__ == "__main__":
    num = int(input("Enter a number-> "))
    multiple_of_10(num)