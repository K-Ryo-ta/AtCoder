N = int(input())
A = [[x for x in input()] for i in range(N)]
B = [[x for x in input()] for i in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i+1,j+1)
           
