year=int(input("请输入年份："))
month=int(input("请输入月份："))
isRn = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(f'{year}年{month}月有31天')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f'{year}年{month}月有30天')
elif isRn:
    print(f'{year}年{month}有29天')
elif not isRn:
    print(f'{year}年{month}有28天')
else:
    print('输入有误')


