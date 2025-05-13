# 练习 3：将此代码封装在名为 count 的函数中，
# 并对其进行泛化，以便它接受字符串和字母作为参数。
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(string, char):
    count = 0
    for letter in string:
        if letter == char:
            count += 1
    return count

print(count("banana", "a"))
print(count("apple", "p"))
print(count("hello", "l"))

