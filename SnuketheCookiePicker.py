a,b= map(int,input().split())
s = [input() for _ in range(a)]
for i in range(0,a):
    for j in range(0,b):
        if s[i][j] == ".":
            if  s[i+1][j] == "#":
                if i==0:
                    print(i,j)
                elif i != 0 and  s[i-1][j] == "#":
                    print(i,j)