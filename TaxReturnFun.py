def Tax(Salary):
    T=Salary*20/100
    return T
Salary=int(input("What is your salary? "))
NetSalary=Salary-Tax(Salary)
print("Tax:",Tax(Salary))
print("Net:",NetSalary)