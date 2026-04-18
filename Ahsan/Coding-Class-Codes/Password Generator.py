import random

def generate_password():
    small_letters="abcdefghijklmnopqrstuvwxyz"
    big_letters="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    numbers="1234567890"
    special_characters="!@#$%^&*()_+"

    all_characters = small_letters+big_letters+numbers+special_characters

    password=list(all_characters)
    random.shuffle(password)
    password=password[:16]

    print ("".join (password))

generate_password()


