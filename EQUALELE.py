#sys.maxsize to learn
import sys
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freqcount = dict.fromkeys(a,0)
    for i in a :
        freqcount[i] +=1
    maxFreq = -(sys.maxsize - 1);
    for key in freqcount:
        maxFreq = max(maxFreq, freqcount[key])
    print(n-maxFreq)