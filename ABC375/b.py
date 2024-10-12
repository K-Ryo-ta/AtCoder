import math

n = int(input())
x = [0.0] * n
y = [0.0] * n

for i in range(n):
    x[i], y[i] = map(float, input().split())

cost = 0.0

cost += math.hypot(x[0], y[0])

for i in range(n - 1):
    cost += math.hypot(x[i + 1] - x[i], y[i + 1] - y[i])

cost += math.hypot(x[n - 1], y[n - 1])

print(cost)

