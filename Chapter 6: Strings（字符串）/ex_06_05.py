# 练习 5：字符串切片
# 采用以下存储字符串的 Python 代码：
# str = 'X-DSPAM-Confidence: 0.8475'
# 使用查找和字符串切片提取字符串中冒号字符之后的部分，然后使用 float 函数将提取的字符串转换为浮点数。

str = 'X-DSPAM-Confidence: 0.8475'

atpos = str.find(' ')

host = str[atpos+1:].strip()

text = float(host)
print(text)