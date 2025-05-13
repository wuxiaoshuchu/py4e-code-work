# 练习3：编写一个提示分数的程序 0.0 到 1.0 之间。如果分数超出范围，则打印错误 信息。
# 如果分数介于 0.0 和 1.0 之间，请使用 下表：
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("enter score : ")
try :
    fscore = float(score)
except :
    print("enter score between 0.0 and 1.0")

if fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")