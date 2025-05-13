# 练习 3：编写一个程序，读取文件并按频率降序打印字母。
# Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
# 您的程序应该将所有输入转换为小写并且仅 数一下字母 az。你的程序不应该计算空格、数字、 标点符号或字母 az 以外的任何内容。查找文本样本 来自几种不同的语言，看看字母频率如何变化 语言之间。将您的结果与https://wikipedia.org/wiki/Letter_frequencies中的表格进行比较。
# Fun fact: The word “tuple” comes from the names given to sequences of numbers of varying lengths: single, double, triple, quadruple, quintuple, sextuple, septuple, etc.↩︎
# 有趣的事实："元组"这个词来自于给定的名称 不同长度的数字序列：单、双、三、 四重、五重、六重、七重等↩︎
# Python does not translate the syntax literally. For example, if you try this with a dictionary, it will not work as you might expect.↩︎
# Python 不会逐字翻译语法。为了 例如，如果你用字典尝试这个，它不会像你那样工作 可能会期待。 ↩︎

text = "Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies."
text = str.lower(text) # 将所有在text中的单词小写

di = dict()
for key in text:
    if key.isalpha(): # 这是 Python 字符串方法的一部分，它用于检查一个字符串是否只包含字母字符。
        if key in di:
            di[key] += 1
        else:
            di[key] = 1 # di[key] = di.get(key, 0) + 1

tmp = list()
for k,v in di.items():
    new_tuple = (k,v) # 将字典转化成元祖
    tmp.append(new_tuple) # 将元祖添加至列表里
tmp = sorted(tmp)
print(tmp)