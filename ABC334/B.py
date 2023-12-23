A,M,L,R = map(int, input().split())
counttree = 0
if A > L and A < R:
    i=0
    while True:
        i += 1
        if A + i * M > R:
            break
        else:
            counttree += 1
        
    i=0
    while True:
        i += 1
        if A - i * M < L:
            break
        else:
            counttree += 1
    print(counttree+1)

elif A < L and A < R:
    i=0
    while True:
        i += 1
        if A + i * M > R:
            break
        elif L  == R:
            break
        else:
            counttree += 1
    print(counttree)

# elif A > L and A > R:      
#     i=0
#     while True:
#         i += 1
#         if A - i * M < L:
#             break
#         elif L == R:
#             break
#         else:
#             counttree += 1
#     print(counttree)
