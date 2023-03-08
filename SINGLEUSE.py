
for i in range(int(input())):
    h, x, y = map(int, input().split())
    h = (h-y)
    count = 1
    while(h>0):
        h = h - x
        count+=1
    print(count)