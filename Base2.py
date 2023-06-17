a=map(int,input().split())
A=0
b=2
c=list(a)
for i in range(0,64):
        if i == 0:
            A += c[i]*1
        elif i == 1:
             A += c[i]*2
        else:
            b = b*2
            A += c[i]*b
print(A)
