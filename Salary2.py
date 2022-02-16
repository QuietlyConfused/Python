Salary=int(input("Enter your salary: £"))
if Salary>=1000:
    if Salary>=2000:
        Tax=Salary*25/100
    else:
        Tax=Salary*15/100
else:
    Tax=0
Net=Salary-Tax
print("Tax is £",Tax)
print("Net salary is £",Net)