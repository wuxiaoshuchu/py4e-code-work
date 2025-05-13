# 练习 1：下载文件的副本
# www.py4e.com/code3/words.txt
# 编写一个程序，读取words.txt中的单词并存储 它们作为字典中的键。
# 价值观是什么并不重要。 然后您可以使用in运算符作为快速检查方法 字符串是否在字典中。

word_dict = {} # 使用其他名字来避免与内置函数类型冲突

file = open("words.txt") # 打开文件

for line in file: # 遍历每一行
    words = line.split() # 将每一行拆分成单词列表

    for word in words: # 遍历每一个单词
        word_dict[word] = True # 将单词作为字典的键，值可以任意，这里用了True

print(word_dict)