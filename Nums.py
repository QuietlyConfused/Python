Nums=[24,3,75,7,13,65,26,96,24]
Counter=1
Big=Nums[0]
while Counter<len(Nums):
    if Nums[Counter]>Big:
        Big=Nums[Counter]
    Counter=Counter+1
print("The highest number is",Big)