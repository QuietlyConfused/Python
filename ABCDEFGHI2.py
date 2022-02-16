Num=int(input("Number: "))
if Num>1000:
    print("A")
    if Num>2000:
        print("C")
        if Num>3000:
            print("H")
        print("M")
    else:
        print("D")
        if Num>1500:
            print("J")
        else:
            print("I")
        print("L")
    print("N")
else:
    print("B")
    if Num>500:
        print("E")
    else:
        print("F")
    print("K")
print("O")
print("P")