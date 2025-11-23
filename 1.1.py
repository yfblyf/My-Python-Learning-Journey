year=int(input("你的出生年份是："))
month=int(input("你的出生月份是："))
day=int(input("你的出生具体日期是："))

count=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    count[1]=29
else:
    count[1]=28
#首先通过列表先设定好每个月的初始天数，接着根据条件判断语句，更改存储二月份天数的位置应该是28还是29


a=day
for i in range(month-1):
    a+=count[i]
#提前将a赋值为天数，则只需将出生月份以前的天数总体相加，相加的程序由循环遍历实现

print("酱酱！宝宝在"+str(year)+"年的第"+str(a)+"天破壳哟૮₍˃̶ꇴ˂̶₎ა")
    
