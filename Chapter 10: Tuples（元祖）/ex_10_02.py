# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# 练习 2：该程序计算 每条消息的一天中的时间。您可以从 通过查找时间字符串然后拆分"From"行 使用冒号字符将字符串分成几部分。一旦你积累了 每小时的计数，打印出计数，每行一个，按 如下图所示的小时。
#
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
open_file = open(fname)

di = dict()
for line in open_file:
     line = line.rstrip()
     if line.startswith("From "):
          words = line.split()
          time = words[5]
          hours = time.split(":")[0]
          di[hours] = di.get(hours, 0) + 1
print(di)

tmp = list()
for k,v in di.items():
    new_tuple = (k,v)
    tmp.append(new_tuple)
tmp = sorted(tmp)

for k,v in tmp:
    print(k,v)
