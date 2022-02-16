def WordCount(Message):
    Counter=0
    Spaces=0
    while Counter<len(Message):
        if Message[Counter]==" ":
            Spaces=Spaces+1
        Counter=Counter+1
    print("In the message we found: ",Spaces+1)
WordCount("Hello my friends")
WordCount("Hello Shafeeq how are you?")