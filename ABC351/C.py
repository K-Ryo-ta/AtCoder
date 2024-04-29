N = int(input())
A = list(map(int, input().split()))

stack = []

for i in range(N):
    ball = 2 ** A[i]
    while stack and stack[-1] == ball:
        ball += stack.pop()
    stack.append(ball)

print(len(stack))
