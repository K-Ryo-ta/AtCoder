n = int(input())
sc = []
for i in range(n):
    sc.append(input().split())

sc_dict = dict(sc)

total = 0
for v in sc_dict.values():
    total += int(v)

sorted_scdict = dict(sorted(sc_dict.items()))

list_sorted_scdict = list(sorted_scdict)

ans = total % n


print (list_sorted_scdict[ans])
