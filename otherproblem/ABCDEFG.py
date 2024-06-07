p,q=input().split()
if (p == "A" and q == "B")or(p == "B" and q == "A"):
    print(3)
elif (p == "A" and q == "C")or(p == "C" and q == "A")or(p == "C" and q == "D")or(p == "D" and q == "C"):
    print(4)
elif (p == "A" and q == "D")or(p == "D" and q == "A"):
    print(8)
elif (p == "A" and q == "E")or(p == "E" and q == "A")or(p == "F" and q == "G")or(p == "G" and q == "F"):
    print(9)
elif (p == "A" and q == "F")or(p == "F" and q == "A")or(p == "E" and q == "G")or(p == "G" and q == "E"):
    print(14)
elif (p == "A" and q == "G")or(p == "G" and q == "A"):
    print(23)
elif (p == "B" and q == "C")or(p == "C" and q == "B")or(p == "D" and q == "E")or(p == "E" and q == "D"):
    print(1)
elif (p == "B" and q == "D")or(p == "D" and q == "B")or(p == "C" and q == "E")or(p == "E" and q == "C")or(p == "E" and q == "F")or(p == "F" and q == "E"):
    print(5)
elif (p == "B" and q == "E")or(p == "E" and q == "B")or(p == "D" and q == "F")or(p == "F" and q == "D"):
    print(6)
elif (p == "B" and q == "F")or(p == "F" and q == "B"):
    print(11)
elif (p == "B" and q == "G")or(p == "G" and q == "B"):
    print(20)
elif (p == "C" and q == "F")or(p == "F" and q == "C"):
    print(10)
elif (p == "C" and q == "G")or(p == "G" and q == "C"):
    print(19)
elif (p == "D" and q == "G")or(p == "G" and q == "D"):
    print(15)

