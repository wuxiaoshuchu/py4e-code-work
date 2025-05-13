# 练习 2：编写另一个程序，提示输入上述数字列表，最后打印出数字的最大值和最小值，而不是平均值。

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or inum > largest:
        largest = inum
    if smallest is None or inum < smallest:
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)