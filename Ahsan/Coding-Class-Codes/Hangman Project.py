import os





if __name__ == "__main__":
    stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """
    ]
    host_word = input("Enter a word -> ")
    display_word = ["_" for l in host_word]
    lives=6
    os.system("cls")
    print ("Welcome to Hangman!")
    is_win=False

    while lives > 0:
        os.system("cls")
        print(f"{stages[lives]}")
        print ("word: "+" ".join(display_word))
        print(f"{lives} attempts remaining.")
        guess=input("Enter a character  -> ")
        if not guess.isalpha() or len(guess) != 1:
            print ("Please enter a valid character!")
        if guess in host_word:
            indices=[i for i, ch in enumerate(host_word) if ch == guess]
            for idx in indices:
                if display_word[idx] == "_":
                    display_word[idx] = guess
                    break
        else:
            lives=lives-1
        if "_" not in display_word:
            is_win=True
            break

    os.system("cls")
    if is_win:
        print(stages[lives])
        print("word: "+" ".join(display_word))
        print("Congratulations, you won!")
    else:
        print(stages[lives])
        print("word: "+" ".join(display_word))
        print("You lost!")
