# 练习 6：用一个半的加班时间重写工资计算，并创建一个名为computepay 的函数
# 该函数采用两个参数（小时和费率）。
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
def computepay(h, r):
    if h < 40:
        tp = h * r
    else :
        tp = (40 * r) + ((h - 40) * r * 1.5 )
    return tp

hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hours: ")

h = float(hrs)
r = float(rate)

p = computepay(h, r)
print("Pay", p)