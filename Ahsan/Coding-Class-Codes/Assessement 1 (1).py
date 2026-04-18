# 1. write a program that input 5 numbers and create a list from those numbers then print them one by one.

# 2. write a program that input 6 numbers 2 names and create a list from it then update the names to any numbers then print them one by one

# 3. write a program that input 5 numbers and create a list of them then remove all elements one by one and print the final list

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

for i in range(0,len(numbers)):
    print(f"{numbers[i]}")