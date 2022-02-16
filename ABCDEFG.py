Num=int(input("Number: "))
if Num>1000:
    print("A")
    if Num>2000:
        print("C")
    else:
        print("D")
else:
    print("B")
    if Num>500:
        print("E")
    else:
        print("F")
print("G")