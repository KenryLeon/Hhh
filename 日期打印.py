#!\usr\bin\env python
# -*- coding:UTF-8 -*-

#月份简写列表
months = [
	'Jan',
	'Feb',
	'Mar',
	'Apr',
	'May',
	'Jun',
	'Jul',
	'Aug',
	'Sep',
	'Oct',
	'Nov',
	'Dec',
]

#以1~31的数字结尾列表
ending = ['st','nd','rd'] + 17 * ['th']\
       + ['st','nd','rd'] + 7 * ['th']\
       + ['st']

#用户输入
year = raw_input('请输入年份:\n')
month = raw_input('请输入月份:\n')
day = raw_input('Day(1~31):\n')

#将输入从str类型转换为int类型
month_number = int(month)
day_number = int(day)

#注意：索引值=实际值-1
month_name = months[month_number-1]
ordinal = day + ending[day_number-1]

print month_name + ','+ ordinal + ','+ year