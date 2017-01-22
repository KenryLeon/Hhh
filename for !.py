#!\usr\bin\env python
# -*- coding:UTF-8 -*-

number = input("输入一个自然数：")
product = 1
for i in range(number):
	product = product * (i + 1)
print product