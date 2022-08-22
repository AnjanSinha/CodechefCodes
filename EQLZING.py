#EQLZING
for i in range(int(input())):
    a, b = map(int, input().split())
    if a>b:
        if (a-b)%2==0: print("Yes")
        else: print("No")
    else: 
        if (b-a)%2==0: print("Yes")
        else: print("No")