def Introduction():
    print("Welcome to the Personalized Adventure Game")
    print("In this game, you'll create your own adventure story.")

def CollectUserInfo():
    name = input("Enter your name ")
    friendName = input("Enter your friend's name ")
    favtPlace = input("Enter your favourite place ")
    return name, friendName, favtPlace

def CreateBeginning(name, friendName):
    print(f"On a sunny, {name} and {friendName} decided to go on an Adventure. ")

def CreateMiddle(favtPlace):
    print(f"They traveled far and wide until they reached {favtPlace}, a place full of mystery and wonder.")

def CreateEnd(name,friendName):
    print(f"In the end, {name} and {friendName} discovered that the true treasure was the friendship they shared.")

def main():
    Introduction()
    name, friendName, favtPlace = CollectUserInfo()
    CreateBeginning(name,frienName)
    CreateMiddle(favtPlace)
    CreateEnd(name,friendName)



