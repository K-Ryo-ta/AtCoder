K,G,M = map(int,input().split())
maxG = G
maxM = M
initialG = 0
initialM = 0
G = initialG
M = initialM

for i in range(K):
    if G == maxG:
        G = 0
    elif M == 0:
        M = maxM
    else:
        z=min(M,maxG-G)
        G,M=G+z,M-z
print(G,M)
