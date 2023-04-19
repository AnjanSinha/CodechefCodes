for i in range(int(input())):
    n, m = map(int, input().split())
    if (m*6*6)>= n :
        print("YES")
    else:
        print("NO")