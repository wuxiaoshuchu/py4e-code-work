# 练习6
# 重写提示用户输入数字列表的程序并 打印出最后数字的最大值和最小值 用户输入"完成"。
# 编写程序来存储用户的号码 输入列表并使用max()和min() 计算循环后的最大和最小数字的函数 完成。
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

lst = [] # 初始化一个空列表来储存用户输入的数字
while True: # 不断提示用户输入，知道输入“done”
    num = input("Enter a number: ")

    if num == "done":
        print("Enter a number: done")
        break

    try:
        num = float(num)
        lst.append(num)
    except:
        print("Please enter a number")

print("Maximun: ",max(lst))
print("Minimun: ",min(lst))