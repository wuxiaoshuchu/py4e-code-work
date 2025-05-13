# 练习1：编写一个重复读取的程序 整数，直到用户输入"done"。
# 输入"完成"后，打印出来 整数的总数、计数和平均值。
# 如果用户输入 除了整数之外的任何东西，使用以下命令检测它们的错误
# try并except并打印错误消息 跳到下一个整数。
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

num = 0
tot = 0.0
while True :
    savl = input('Enter a number: ')
    if savl == 'done':
        break
    try:
        favl = float(savl)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + favl
print(tot,num,tot/num)