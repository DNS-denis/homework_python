from datetime import date, timedelta

def dictionary(data, notes):
    t = timedelta(days=1)
    o = open("captain's notes.txt", "w")
    for note in notes:
        o.write(str(data) + ': ' +  note + '\n')
        data += t
    o.close()

dictionary(date(2022, 12, 13), ["Сегодня я попал на остров", "На данный момент смастерил шалаш"]) 
