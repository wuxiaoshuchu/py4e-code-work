# 练习 2：编写一个程序，对每个类别进行分类 邮件消息在一周中的哪一天完成提交。
# 要做到这一点 查找以"From"开头的行，然后查找第三个单词并 对一周中的每一天进行连续计数。结束时 程序打印出字典的内容（顺序不 事情）。
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Sample Execution:示例执行：
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

import string
words_dict = {}

fname = input("Enter a file name:")

open_file = open(fname)

for line in open_file:
    line = line.rstrip()
    if line.startswith("From"):
        words = line.split()
        if len(words) >= 3:
            day_of_week = words[2]
            if day_of_week not in words_dict:
                words_dict[day_of_week] = 0
        else:
            words_dict[day_of_week] += 1

print(words_dict)



