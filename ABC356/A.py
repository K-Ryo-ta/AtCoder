N,L,R = map(int,input().split())
A = []

for i in range(1, N +1):
    A.append(i)

while L < R:
    A[L-1], A[R-1] = A[R-1], A[L-1]
    L += 1
    R -= 1

print(*A)
