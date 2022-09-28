# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year_num = int(input('Введите номер года '))
if year_num > 0:
    x = (year_num // 100)*100
    if x == year_num:
        century_num = year_num // 100
        print(year_num, 'год это', century_num, 'столетие')
    else:
        century_num = year_num  // 100 + 1
        print(year_num , 'год это', century_num, 'столетие')
else:
    print('Не корректно веден год')