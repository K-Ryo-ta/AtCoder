A,M,L,R = map(int, input().split())
L -= A
R -= A
print(R//M - (L-1)//M)
