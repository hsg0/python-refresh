# sallary based years of experience
def salary(years):
    baseSalary = 25000
    if years >= 2 and years <= 4:
        # raise of 1.5x and 500 bonus
        baseSalary *= 1.5
        baseSalary += 500
    elif years > 4 and years <= 10:
        # raise of 2x and 1000 bonus
        baseSalary *= 2
        baseSalary += 1000
    elif years > 10:
        # raise of 3x and 2000 bonus
        baseSalary *= 3
        baseSalary += 2000
    else:
        # no raise only bonus
        baseSalary += 250
    return baseSalary