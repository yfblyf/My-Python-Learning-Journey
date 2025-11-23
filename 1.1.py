year=int(input("你的出生年份是："))
month=int(input("你的出生月份是："))
day=int(input("你的出生具体日期是："))

count=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    count[1]=29
else:
    count[1]=28

a=day
for i in range(month-1):
    a+=count[i]

print("酱酱！宝宝在"+str(year)+"年的第"+str(a)+"天破壳哟૮₍˃̶ꇴ˂̶₎ა")
    

