while True:
    n, p = map(int, input().split())
    if n == 0:
        break
    ans, m = 0, p
    a=[0]*53
    while True:
        m-=1
        if m >= 0:
            a[ans] += 1
            if a[ans]==p:
                break
        else: m=a[ans];a[ans]=0
        ans+=1
        if ans == n: ans=0
    print(ans)
