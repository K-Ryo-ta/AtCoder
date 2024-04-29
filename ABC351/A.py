A = map(int,input().split())
B = map(int,input().split())

sumA = sum(A)
sumB = sum(B)

if sumA > sumB:
    print(sumA - sumB + 1)
else:
    print(1)
