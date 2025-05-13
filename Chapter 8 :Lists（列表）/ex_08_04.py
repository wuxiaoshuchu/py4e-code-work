# 练习 4：查找文件中的所有唯一单词
# 莎士比亚在他的作品中使用了两万多个单词。但你会怎样 确定那个？您将如何生成所有单词的列表 用过莎士比亚吗？
# 你会下载他的所有作品，阅读并追踪所有作品吗？ 手工独特的单词？
# 让我们使用 Python 来实现这一点。列出存储在包含莎士比亚作品子集的文件 romeo.txt 中的所有唯一单词（按字母顺序排序）。
# 首先，下载文件www.py4e.com/code3/romeo.txt的副本。 创建一个唯一单词列表，其中将包含最终结果。
# 编写一个程序来打开文件romeo.txt并读取它的行 按行。对于每一行，使用以下命令将该行拆分为单词列表 split功能。
# 对于每个单词，检查该单词是否是 已经在独特单词列表中。如果该单词不在列表中 独特的单词，将其添加到列表中。当程序完成后，排序并 按字母顺序打印唯一单词的列表。
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

final_list = []
file = input("Enter file:")
open_file = open(file)

for line in open_file:
    words = line.split()
    for word in words:
        if word not in final_list:
            final_list.append(word)

final_list.sort()
print(final_list)