# 练习 2：将该程序的最后一行移至顶部，以便函数调用出现在定义之前。
# 运行该程序并查看收到的错误消息。

repeat_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# NameError: name 'repeat_lyrics' is not defined
