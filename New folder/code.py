with open("file1.txt","r") as file1:
    data = file1.read()

name = "My name is "+data
print(name)

with open("file2.txt",'r') as file2:
    file2.write(name+'\n')

    










