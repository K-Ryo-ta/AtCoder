N = input()
A = list(map(int,input().split()))
max = 0
secondmax = 0

for i in range(int(N)):
    if A[i] > max:
        max = A[i]

for i in range(int(N)):
    if A[i] != max and A[i] > secondmax:
        secondmax = A[i]

print(secondmax)
