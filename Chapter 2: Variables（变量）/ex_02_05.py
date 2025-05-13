# 练习 5：编写一个程序，提示用户输入摄氏温度，将温度转换为华氏温度，并打印出转换后的温度。
celsius = input('enter celsius degrees: ')
f_celsius = float(celsius)
fahrenheit = f_celsius * 9 / 5 + 32
print('fahrenheit degree is:', fahrenheit)