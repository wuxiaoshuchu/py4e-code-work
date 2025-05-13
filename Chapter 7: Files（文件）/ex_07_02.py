# 练习 2：编写一个程序以提示输入文件名，然后读取文件并查找以下格式的行：
# X-DSPAM-Confidence: 0.8475
# 当你遇到以"X-DSPAM-Confidence:"开头的行时，拆分 该行以提取行中的浮点数。计算 这些行的数量，然后计算这些行中垃圾邮件置信值的总和。到达文件末尾时，打印出 平均垃圾邮件置信度。
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
#
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519


fx = input("Enter the file name: ")
fh = open(fx)
total = 0
count = 0
for lx in fh:
    ly = lx.strip()
    if ly.startswith("X-DSPAM-Confidence"):
        confidence = float(ly.split(":")[1].strip())
# #分割字符串
# ly.split(":") 会把字符串按照冒号 ":" 分割成一个列表。
# 在这个例子中，ly.split(":") 会产生这个列表：
# 列表的第一个元素是 'X-DSPAM-Confidence'，第二个元素是 ' 0.8475'。
# 选择数值部分
# ly.split(":")[1] 获取了分割后列表的第二个元素，即 ' 0.8475'（列表是从 0 开始编号的，所以 [1] 表示第二个元素）。
# 去除空格
# ly.split(":")[1].strip() 去掉数值部分的前后空格，得到 '0.8475'。
# 转换为浮点数
# float(ly.split(":")[1].strip()) 将字符串 '0.8475' 转换成浮点数 0.8475。
        count = count + 1
        total += confidence
print("Average spam confidence: ",float(total/count))

