# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# 练习 1：按如下方式修改以前的程序：读取并解析"From"行，并从该行中提取地址。使用字典计算每个人的消息数量。
#
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
# 所有数据读完后，打印最多的人 通过从字典中创建（计数，电子邮件）元组列表来提交。 然后对列表进行倒序排序，并打印出拥有该人的人 大多数提交。
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195


fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
open_file = open(fname)

di = dict()
for line in open_file:
     line = line.rstrip()
     if line.startswith("From "):
          words = line.split()
          email = words[1]
          di[email] = di.get(email,0) + 1
# print(di)

tmp = list()
for k,v in di.items():
    new_tuple = (v,k)
    tmp.append(new_tuple)
tmp = sorted(tmp, reverse=True)
most_commit = tmp[0]
v,k = most_commit
print(k,v)
