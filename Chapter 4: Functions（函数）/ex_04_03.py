# 练习3：将函数调用移回底部，并将print_lyrics 的定义移到repeat_lyrics 的定义之后。
# 当你运行这个程序时会发生什么？
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()