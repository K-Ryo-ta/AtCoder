s = input()
slist = list(s)
countbig = 0
countsmall = 0

for i in range(len(slist)):
    if(slist[i].islower()):
        countsmall += 1
    else:
        countbig += 1

for i in range(len(slist)):
    if countbig > countsmall:
        slist[i] = slist[i].upper()
    else :
        slist[i] = slist[i].lower()

print(''.join(slist))
