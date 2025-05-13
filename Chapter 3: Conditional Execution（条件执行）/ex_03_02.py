# 练习 2：使用以下方法重写您的薪酬计划 try并except以便您的程序处理
# 通过打印消息并退出来优雅地进行非数字输入 程序。下图展示了程序的两次执行：
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

sh = input("enter the hours:")
sr = input("enter the rate:")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("error, please enter numeric number")
    quit()

if fh > 40 :
    reg = fr * fh
    otp = (fh -40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("your pay is :",xp)