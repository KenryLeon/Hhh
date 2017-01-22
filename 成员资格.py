#!\usr\bin\env python
# -*- coding:UTF-8 -*-

#用户名与密码数据
database = [
	['Liang Kunyi','990612']
]

#输入
username = raw_input('User name:\n')
password = raw_input('Passord:\n')

#验证
if [username,password] in database:
	print 'Welcome!!!'
else:
	print 'Hello...'