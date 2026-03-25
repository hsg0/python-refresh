from salary import salary
from hourly import partTime, fullTime

startQuit = int(input("welcome, press '1' or any key to start, or type '0' to quit: "))
while startQuit != 0:
    employeeName = input("Enter employee name: ")
    employeeType = input("Is the employee on salary or hourly? (salary/hourly): ").lower()
    if employeeType == 'hourly':
        hoursWorked = float(input("Enter hours worked: "))
        if hoursWorked > 0 and hoursWorked < 35:
            pay = partTime(hoursWorked)
            print(pay)
        elif hoursWorked >= 40:
            pay = fullTime(hoursWorked)
            print(pay)
        else:
            print("Invalid hours worked. Please enter a positive number.")
    elif employeeType == 'salary':
        yearsExperience = int(input("Enter years of experience: "))
        if yearsExperience >= 0:
            pay = salary(yearsExperience)
            print(pay)
        else:
            print("Invalid years of experience. Please enter a non-negative number.")
    else:
        print("Invalid employee type. Please enter 'salary' or 'hourly'.")
    startQuit = int(input("Press '1' to start again, or type '0' to quit: "))
print("Goodbye!")
            