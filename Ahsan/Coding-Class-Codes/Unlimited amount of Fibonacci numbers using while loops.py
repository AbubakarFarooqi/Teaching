lst=[0,1]
i=2
a=int(input("Enter your limit here -> "))

while i<a:
    new=lst[i-1]+lst[i-2]
    lst.append (new)
    i=i+1
print(lst)
