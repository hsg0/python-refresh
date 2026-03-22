# expence tracker
# inflows
income = int(input("Enter your income: "))
windfall = int(input("Enter your windfall: "))
# outflows
food = int(input("Enter your food expenses: "))
rent = int(input("Enter your rent expenses: "))
utilities = int(input("Enter your utilities expenses: "))
entertainment = int(input("Enter your entertainment expenses: "))
extra = int(input("Enter your extra expenses: "))
# calculate total inflows and outflows
totalInflows = income + windfall
totalOutflows = food + rent + utilities + entertainment + extra
# calculate net cash flow
netCashFlow = totalInflows - totalOutflows
# print the result
print("Your net cash flow is:", netCashFlow)