# 练习 1：编写一个while循环 从字符串中的最后一个字符开始并向后移动 到字符串中的第一个字符，
# 将每个字母打印在单独的 线，除了向后。
# 编写遍历的另一种方法是使用 for 循环：
# for char in fruit:
#     print(char)
# 每次循环时，字符串中的下一个字符都会分配给变量
# char。循环继续，直到没有剩余字符为止。

fruit = "apple"
index = len(fruit) - 1  # 从最后一个字符开始

while index >= 0:
    print(fruit[index])  # 输出当前字符
    index -= 1  # 将索引值向前移动

for char in fruit:
    print(char)

