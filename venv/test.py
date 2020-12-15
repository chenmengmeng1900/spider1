year = int(input("请输入年份："))  #先输入一个年份
ly = False  #定义一个bool值



if year< 9999:
    if year % 100 == 0:
        if year % 400 == 0:
            ly = True
        else:
            ly = False
    elif year % 4 == 0:
        ly = True
    else:
        ly = False


#然后用ly是做判断。if  ly是true则选择闰年，否则选择平年

if ly:
    month_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
else:
    month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}



m = int(input("请输入月份："))
d = int(input("请输入日期："))
if m not in month_day:
    print("月份输入有误!")
    exit(1)

if d < 1 or d > month_day[m]:
    print("您输入的日期有误：")
    exit(1)

days = 0
for i in range(1, m):
    days += month_day[i]
print('这是闰年的第%s天' % (days+d))