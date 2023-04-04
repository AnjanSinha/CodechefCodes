for i in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    minimum = min(arr)
    cout = 0
    for i in arr:
        if (i!=minimum):
            cout+=1
    print(cout)