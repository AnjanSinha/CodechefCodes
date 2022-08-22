#CANDYDIST
for i in range(int(input())):
    n, m = map(int, input().split())
    if n%m==0:
        if (n//m)%2==0:
            print("Yes")
        else: 
            print("No")
    else: 
        print("No")