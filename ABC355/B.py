n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a + b)

is_consecutive = False
for i in range(n + m - 1):
    if c[i] in a and c[i + 1] in a:
        is_consecutive = True
        break

if is_consecutive:
    print("Yes")
else:
    print("No")
