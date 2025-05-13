# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.
# 练习5：该程序记录域名 （而不是地址）消息是从哪里发送的而不是由谁发送 邮件来自（即整个电子邮件地址）。结束时 程序，打印出字典的内容。
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

email_dict = {}
fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
open_file = open(fname)

for line in open_file:
     line = line.rstrip()
     if line.startswith("From "):
          words = line.split()
          email = words[1]
          domain = email.split('@')[1] # 这一步非常重要！！！！因为邮件被提出之后还想进行分割就用这个
          # if domain not in email_dict: # 这里是检查domain（键）是否在字典中
          #      email_dict[domain] = 1
          # else:
          #      email_dict[domain] += 1
          di[domain] = di.get(domain, 0) + 1 # 可以直接用这一行代码代替
print(email_dict)