N = int(input())
A = list(map(int, input().split()))
Ans = False
same = A[0]

for i in range(N):
    if A[i]  == same:
        Ans = True
    else:
        Ans = False
        break

if Ans == True:
    print("Yes")
else:
    print("No")
