Salary=int(input("The salary is: £"))
if Salary>=2000:
    Tax=Salary*20/100
    Net=Salary-Tax
if Salary<2000:
    Tax=Salary*10/100
    Net=Salary-Tax
print("so the tax is: £",Tax,"and the Net salary is: £",Net)
