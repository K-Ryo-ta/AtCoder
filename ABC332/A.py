N,S,K = map(int,input().split())
PQ = [(map(int, input().split()))for _ in range(N)]
P,Q = [list(i) for i in zip(*PQ)]
A = 0

for i in range(N):
    s = P[i]*Q[i] 
    A += s
if A < S:
    A += K
print (A)

