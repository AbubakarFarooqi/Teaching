import os
import time

stages = [ 
     """ 
    ----------
    |      |
    |      O
    |     /|\\
    |     / \\
    |
---------------
    """   
    ,
    """ 

    ----------
    |      |
    |      O
    |     /|\\
    |     /
    |
---------------
    """,    
    """ 
    ----------
    |      |
    |      O
    |     /|\\
    |     
    |
---------------
    """,    
    """ 
    ----------
    |      |
    |      O
    |     /|
    |     
    |
---------------
    """,    
    """ 
    ----------
    |      |
    |      O
    |      |
    |
    |
---------------
    """,    
    """ 
    ----------
    |      |
    |      O
    |
    |
    |
---------------
    """,    
    """ 
    ----------
    |      |
    |
    |
    |
    |
---------------
    """,
]

host_word=input("Please enter a host word-> ")
display_word=['_' for i in range(len(host_word))]
attempts=6

def check_for_dash(list):
    for element in list:
        if element == '_':
            return True
    return False
    
while attempts > 0:
    os.system("cls")


    print(stages[attempts-1])

    print(' '.join(display_word))


    guess=input("Enter a character-> ")

    if not guess.isalpha() or len(guess)!=1:
        print("Please enter a valid character!")
        time.sleep(3)
    if guess in host_word:
        indices=[i for i,ch in enumerate(host_word) if ch == guess]
        for i in indices:
            if display_word[i] == '_':
                display_word[i] = guess
                break
    else:
        attempts=attempts-1
    
    if not check_for_dash(display_word):
        break


if attempts == 0:
    os.system("cls")
    print(stages[0])
    print(' '.join(display_word))
    print("You Lose!!")
else:
    os.system("cls")
    print(stages[attempts-1])
    print(' '.join(display_word))
    print ("You Win!!!")