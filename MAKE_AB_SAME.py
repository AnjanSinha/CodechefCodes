for i in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if A == B:
        print("Yes")
    else:
        for i in range(N):
            if (A[i]!=B[i]):
                if (i == 0 or i ==(N-1)):
                    break
                else:
                    A[i] = A[i-1] | A[i] | A[i+1]
        if (A ==B):
            print("Yes")
        else:
            print("No")