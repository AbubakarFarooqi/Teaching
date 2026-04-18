import random

def password_generator():
    num=int(input("Enter your character limit -> "))
    small_letters="abcdefghijklmnopqrstuvwxyz"
    big_letters="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    numbers="1234567890"
    symbols="!@#$%^&*()_+"

    all_characters=small_letters+big_letters+numbers+symbols

    password=list(all_characters)
    random.shuffle(password)
    password=password[:num]

    print("".join (password))

password_generator()
