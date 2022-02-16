def Printing(Message):
    Word=" "
    Counter=len(Message)-1
    while Counter>=0:
        if Message[Counter]==" ":
            print(Word)
            Word=" "
        else:
            Word=Message[Counter]+Word
        Counter=Counter-1
    print(Word)
Printing("My name is Stew and I am learning Python")