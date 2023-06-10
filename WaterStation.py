n = int(input())
i = 0
while (n+i)%5!=0:
    i+=1
j=5
while (n-j)%5!=0:
    j-=1
if i>j:
    print(n-j)
else:
    print(n+i)
    