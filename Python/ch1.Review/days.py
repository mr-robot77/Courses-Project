from datetime import datetime

def day_calculator(date):
    date = datetime.strptime(date , '%Y-%m-%d')
    print("day:", date.day)
    print("month:", date.month)
    print("year:", date.year)
    sajjad_bdate = datetime.strptime("1999-01-14",'%Y-%m-%d')
    d = (date - sajjad_bdate).days
    if d < 0:
        return 'Not yet born'
    else:
        return d