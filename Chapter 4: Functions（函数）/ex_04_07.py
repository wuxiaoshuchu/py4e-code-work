# 练习 7：使用名为computegrade 的函数重写上一章的成绩程序
# 该函数将分数作为参数并以字符串形式返回成绩。
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("enter score : ")
try:
    s = float(score)
except:
    print("enter score between 0.0 and 1.0")
    s = None
def computergrade(s):
    if s >= 0.9 :
        return "A"
    elif s >= 0.8 :
        return "B"
    elif s >= 0.7 :
        return "C"
    elif s >= 0.6 :
        return "D"
    else :
        return "F"

if s is not None:
    print('Grade: ',computergrade(s))