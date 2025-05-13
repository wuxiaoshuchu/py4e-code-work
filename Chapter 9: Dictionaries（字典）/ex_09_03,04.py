# 练习 3：编写一个程序来读取邮件日志，使用字典构建直方图来计算来自每个电子邮件地址的消息数量，然后打印字典。
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

email_dict = {}
fname = input("Enter file name: ")
open_file = open(fname)

for line in open_file:
     line = line.rstrip()
     if line.startswith("From "):
          words = line.split()
          email = words[1]
          if email not in email_dict:
               email_dict[email] = 1
          else:
               email_dict[email] += 1
print(email_dict)


# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
# 练习4：在上面的程序中添加代码来计算 找出文件中谁拥有最多的消息。全部数据完成后 read 字典已经创建，查看字典 使用最大循环（参见第 5 章：最大和最小循环）来查找 谁拥有最多的消息并打印该人有多少条消息 有。
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

most_messages = None
most_emails_count = 0

# 使用最大循环查找最大值
for email in email_dict: # 使用字典的键来遍历并查找最大值
     count = email_dict[email] #获取当前邮件地址的邮件数量
     if count > most_emails_count:
        most_messages = email
        most_emails_count = count

print(most_messages, most_emails_count) # 打印拥有最多邮件的用户及其邮件数量