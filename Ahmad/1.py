lst = [5,4,3,2,1]
def min_l(l,j):
    min = l[j]
    min_idx = j
    for i in range (j,len(l)):
        if l[i] < min:
            min = l[i]
            min_idx = i
    return min,min_idx


for i in range (0,len(lst)-1):
    min,min_idx = min_l(lst,i)
    x =lst[i]
    lst[i] = min
    lst[min_idx] = x 
print(lst)