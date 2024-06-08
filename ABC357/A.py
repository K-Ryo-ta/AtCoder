n,m = map(int,input().split())
h = list(map(int,input().split()))

ans = 0

for i in range(n):
    if(m - h[i] == 0):
        ans = i
        break
    elif(m - h[i] < 0):
        ans = i - 1
        break

    m -= h[i]
    ans = i

print(ans + 1)
