# 练习 1：编写一个名为 chop接受一个列表并修改它，删除第一个 和最后一个元素，并返回None 。
# 然后写一个函数 称为middle ，它接受一个列表并返回一个新列表 包含除第一个和最后一个元素之外的所有元素。

def chop(list):
    if len(list) > 1:
        del list[0]
        del list[-1]
        return list
    else:
        return None

def middle(list):
    return list[1:-1]

list = [1,2,3,4,5,6,7,8]
new_list1 = chop(list)
new_list2 = middle(list)

print(new_list1)
print(new_list2)

