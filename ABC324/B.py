N = int(input())

while True:
    if (int(N)%2 == 0):
        N:int = int(N)/2
    else:
        break

while True:
    if (int(N)%3 == 0):
        N:int = int(N)/3
    else:
        break
    
if (N == 1):
    print("Yes")
else:
    print("No")
