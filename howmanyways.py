def solve():
    a,b =map(int,input().split())
    if (a == 0 and b == 0) or a == 2:
        return False
    count = 0
    for i in range(1,a+1):
        for j in range(1,i):
            for k in range(1,j):
                if i+j+k==b:
                    count += 1
    print(count)
    return True

while solve():
    pass

    
