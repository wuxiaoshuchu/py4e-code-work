# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])
# 练习 3：重写上例中的监护人代码，不使用两个 if 语句。相反，应使用将 or 逻辑运算符与单个 ​​if 语句结合使用的复合逻辑表达式。

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' : continue
    print(words[2])