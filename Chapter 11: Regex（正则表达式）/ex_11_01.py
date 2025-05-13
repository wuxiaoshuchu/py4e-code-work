# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# 练习1：编写一个简单的程序来模拟Unix上grep命令的操作。
# 要求用户输入正则表达式并计算与正则表达式匹配的行数：
#
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
#
# $ python grep.py
# Enter a regular expression: # Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# # 练习1：编写一个简单的程序来模拟Unix上grep命令的操作。
# # 要求用户输入正则表达式并计算与正则表达式匹配的行数：
# #
# # $ python grep.py
# # Enter a regular expression: ^Author
# # mbox.txt had 1798 lines that matched ^Author
# #
# # $ python grep.py
# # Enter a regular expression: ^X-
# # mbox.txt had 14368 lines that matched ^X-
# #
# # $ python grep.py
# # Enter a regular expression: java$
# # mbox.txt had 4175 lines that matched java$
#
#
# import re
# exp = input("Enter a regular expression: ")
# hand = open('mbox.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall(pattern=exp,line)
#     if len(x) > 0:
#         print(x)
# print('mbox.txt had',len(x),'lines that matched',exp)
# mbox.txt had 14368 lines that matched ^X-
#
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$


import re
# 获取用户输入的正则表达式
exp = input("Enter a regular expression: ")
hand = open('mbox.txt')
# 初始化计数器
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(exp, line):
        count += 1
print('mbox.txt had',count,'lines that matched',exp)
# 感想：从最开始我的想法就错了，用len(x)是不正确的