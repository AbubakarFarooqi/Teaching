def add(n1,n2,*args):
    sum = n1+n2
    for i in args: # args = [1,1]
        sum += i
    print(sum)

add(2,3,1,7,8)