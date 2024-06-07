n = int(input())
a = map(int,input().split())
b = list(a)
ans = []
cnt =[0 for _ in range(3*n)]
for i in b:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)

print(*ans)
                




