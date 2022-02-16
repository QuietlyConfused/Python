def Salaryslip(Name,Salary):
        if Salary>=2000:
            Tax=Salary*20/100
        else:
            Tax=Salary*15/100
        NetSalary=Salary-Tax
        print("Name of employee:",Name)
        print("Salary:",Salary)
        print("Tax:",Tax)
        print("Net Salary:",NetSalary)
Salaryslip("Stew",2000)
Salaryslip("James",1500)