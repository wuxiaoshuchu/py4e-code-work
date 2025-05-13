# Exercise 2: Write a program to look for lines of the form:
# 练习 2：编写一个程序来查找以下形式的行：
#
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
# 使用正则表达式和 findall() 方法从每行中提取数字。计算数字的平均值并将平均值作为整数打印出来。
#
# Enter file:mbox.txt
# 38549
#
# Enter file:mbox-short.txt
# 39756


import re

file = input('Enter file:')
hand = open(file)

num = []
for line in hand:
    line = line.rstrip()
    x= re.findall('^New.*: ([0-9]+)', line) # 在数字那（），这样返回出的只有数字
    if x : # if x 是为了防止没有返回值，导致空列表的情况。如果x不是空列表，才会进行下一步操作
        num.append(int(x[0])) # 如果没有if x 会出现out of range的情况

avg = sum(num) //len(num)
print(avg)

