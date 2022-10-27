def dateValidate(day, month, year):
    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    if month in d31:
        return 1 <= day <= 31
    elif month in d30:
        return 1 <= day <= 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return month == 2 and 1 <= day <= 29
    else:
        return month == 2 and 1 <= day <= 28
