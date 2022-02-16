Bill=int(input("How much is your bill? "))
Paid=int(input("How much did they pay? "))
Balance=Paid-Bill
if Balance>=50:
    Fifty=int(Balance/50)
    print("£50 notes: ",Fifty)
    Balance=Balance-(Fifty*50)
if Balance>=20:
    Twenty=int(Balance/20)
    print("£20 notes: ",Twenty)
    Balance=Balance-(Twenty*20)
if Balance>=10:
    print("£10 notes: ",1)
    Balance=Balance-10
if Balance>=5:
    print("£5 notes: ",1)
    Balance=Balance-5
if Balance>=2:
    Two=int(Balance/2)
    print("£2 coins: ",Two)
    Balance=Balance-(Two*2)
if Balance>=1:
    print("£1 coins: ",1)
print("The balance should now be zero,",Balance)

