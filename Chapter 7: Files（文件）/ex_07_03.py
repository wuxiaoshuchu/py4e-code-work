# Exercise 3:练习 3:
# 有时，当程序员感到无聊或想要玩得开心时， 他们会在程序中添加一个无害的彩蛋。修改这个 提示用户输入文件名的程序，使其在用户输入确切的文件名"na na boo boo"时打印一条 有趣的消息。对于所有其他存在和不存在的文件，程序应正常运行。以下是程序的示例执行：
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
#
# Enter the file name: missing.txt
# File cannot be opened: missing.txt
#
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!


fx = input("Enter the file name: ")
count = 0
if fx == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        fh = open(fx)
        for x in fh:
            lx = x.strip()
            count += 1
        print("There were",int(a),"subject lines in mbox.txt")
    except:
        print("File cannot be opened:",fx)