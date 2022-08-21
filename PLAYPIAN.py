# PLAYPIAN
for _ in range(int(input())):
    s = str(input())
    lis =[]
    for i in s:
        lis.append(i)
    cout = 1
    for j in range(len(lis)-1):
        if j%2==0:
            if lis[j]==lis[j+1]:
                cout=0
                break
            else: continue
    if cout==1: print('yes')
    else: print('no')
    
        
            