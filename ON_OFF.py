#ON_OFF
for _ in range(int(input())):
    n = int(input())
    s = str(input())
    r = str(input())
    lis=[]
    lir=[]
    for i in s:
        lis.append(i)
    for j in r:
        lir.append(j)
    cout = 0
    for k in range(n):
        if lis[k]!=lir[k]:
            cout +=1 
        else: continue
    if cout%2==0: print(1)
    else: print(0)
            
        