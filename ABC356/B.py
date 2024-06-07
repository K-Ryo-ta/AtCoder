N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [[int(x) for x in input().split()] for i in range(N)]
sum = 0
count = 0

for j in range(M):
    for i in range(N):
        sum += B[i][j]
    if sum >= A[j]:
        count += 1
    sum = 0

if count == M:
    print("Yes")
else:
    print("No")
