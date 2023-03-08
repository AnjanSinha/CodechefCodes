for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if (a[i]>(b[i]*2)):
            continue
        elif(b[i]>(a[i]*2)):
            continue
        else:
            count +=1
    print(count)
