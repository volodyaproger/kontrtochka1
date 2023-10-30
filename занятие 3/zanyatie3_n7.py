def F(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        print('ДA')
    else:
        print('НET')

year = int(input())
F(year)
