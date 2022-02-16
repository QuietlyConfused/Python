def Printing(Message):
    Word=" "
    Counter=0
    while Counter<len(Message):
        if Message[Counter]==" ":
            print(Word)
            Word=" "
        else:
            Word=Word+Message[Counter]
        Counter=Counter+1
    print(Word)
Printing("My name is Stew and I am learning Python")