# 练习 1：重写工资计算，对于工作时间超过 40 小时的员工，给予 1.5 倍的小时工资。
sh = input("enter the hours:")
sr = input("enter the rate:")
fh = float(sh)
fr = float(sr)
if fh > 40 :
    reg = fr * fh
    otp = (fh -40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("your pay is :",xp)