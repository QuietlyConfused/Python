Uniquewords=[]

def findUnique(Word):
    for w in Uniquewords:
        if w==Word:
            return False
    Uniquewords.append(Word)
    return True

def removeduplicates(Msg):
    NewMsg=" "
    Word=" "
    Counter=0
    while Counter<len(Msg):
        if Msg[Counter]==" ":
            if findUnique(Word):
                NewMsg=NewMsg+Word
            Word=" "
        else:
            Word=Word+Msg[Counter]
        Counter=Counter+1
    if findUnique(Word):
        NewMsg=NewMsg+Word
    print(NewMsg)

removeduplicates("My name is name is Stew")