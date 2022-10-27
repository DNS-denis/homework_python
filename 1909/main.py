def dateValidate(day, month, year):
    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    if month in d31:
        if 1 <= day <= 31:
            return True
        else:
            return False
    elif month in d30:
        if 1 <= day <= 30:
            return True
        else:
            return False
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2 and 1 <= day <= 29:
            return True
        else:
            return False
    elif month == 2 and 1 <= day <= 28:
        return True
    else:
        return False
