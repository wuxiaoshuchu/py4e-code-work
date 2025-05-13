#练习 3：编写一个程序来提示用户输入小时数和每小时费率，以计算总工资。
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
hrs = input('working hours: ')
rts = input('working rates: ')
float_hrs = float(hrs)
float_rts = float(rts)
pay = float_hrs * float_rts
print('pay:',pay)