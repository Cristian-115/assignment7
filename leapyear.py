def isleap(year):
    array = []
    if year < 0:
        array.append("year was not positive")
    if year % 4 == 0 and year % 100 != 0:
        array.append(str(year) + " is a leap year")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        array.append(str(year) + " is a leap year!")

    else:
        array.append(str(year) + " not a leap year")
    return array