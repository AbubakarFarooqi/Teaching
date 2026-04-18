lst=[0,1]
i=2
num=int(input("Enter a number here -> "))

while i<num:
    new=lst[i-1]+lst[i-2]
    lst.append (new)
    i=i+1
print (lst)

