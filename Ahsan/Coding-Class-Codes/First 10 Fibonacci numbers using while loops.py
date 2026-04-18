lst=[0,1]
i=2

while i<10:
    new=lst[i-1]+lst[i-2]
    lst.append (new)
    i=i+1
print(lst)
