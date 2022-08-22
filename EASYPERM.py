# EASYPERM
for i in range(int(input())):
    n= int(input())
    lenn=n
    b=[]
    while n>0:
        b.append(n)
        n-=1 
    for i in range(lenn):
        print (b[i], end=" ")