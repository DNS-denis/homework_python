from datetime import date, timedelta

def dictionary(data, notes):
    a = timedelta(days=1)
    o = open("file.txt", "w")
    for note in notes:
        o.write(str(data) + ': ' +  note + '\n')
        data += a
    o.close()

dictionary(date(2022, 12, 12), ["ihgov", "wef", "ewf"])