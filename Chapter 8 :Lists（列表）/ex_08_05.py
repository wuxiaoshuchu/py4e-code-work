# 练习 5：极简电子邮件客户端。
# MBOX（邮箱）是一种流行的文件格式，用于存储和共享电子邮件的集合。这是早期电子邮件服务器和桌面使用的 应用程序。无需赘述，MBOX 是一个文本文件， 连续存储电子邮件。电子邮件由特殊线分隔 以From开头（注意空格）。
# 重要的是， 以From:注意冒号）开头的行描述了 电子邮件本身并不充当分隔符。想象一下你写了一个极简主义电子邮件应用程序，在用户的列表中列出发件人的电子邮件 收件箱并计算电子邮件数量。
# 编写一个程序来读取邮箱数据，当你发现 以"From"开头的行，您将使用以下命令将该行拆分为单词 split函数。我们感兴趣的是是谁发送的 message，这是发件人行的第二个单词。
# 您将解析 From 行并打印出每个的第二个单词 From line，那么您还将计算 From （不是 From:) 行数 并在最后打印出计数。这是一个很好的示例输出 删除了几行：
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
#
# [...some output removed...]
#
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

count = 0
inp = input("Enter a file name:")
open_inp = open(inp)

for line in open_inp:
    if line.startswith("From "): # 只处理From 开头的行
        words = line.split()
        email = words[1] # 提取第二个单词（邮箱地址）
        print(email)
        count += 1
print("There were",count,"lines in the file with From as the first word")