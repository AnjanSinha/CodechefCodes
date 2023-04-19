
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    array = []
    array.append(abs(a[0]-a[1]))
    array.append(abs(a[n-1]-a[n-2]))
    for j in range(1,n-1):
        array.append(max(abs(a[j]-a[j-1]),abs(a[j]-a[j+1])))
    print(min(array))