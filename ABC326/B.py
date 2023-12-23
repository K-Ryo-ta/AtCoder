import math
A,M,L,R = map(int, input().split())

r = R - A
l = A - L

if A < L:
    print(math.ceil(r/M) + math.ceil(l/M)-1)
else:
    print(math.ceil(r/M) + math.ceil(l/M))

