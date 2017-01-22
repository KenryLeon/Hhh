#hello.py
#!\usr\bin\env python
# -*- coding:UTF-8 -*-

print ('\n\n\n\n')

e = raw_input('Your computer son: Do you really want a girlfriend?\n\n' )
print ('\n\n\n\n')

d = raw_input('Your computer son: Do you feel so lonely? \n\n')
print ('\n\n\n\n')

a = raw_input('Your computer son: So how tall are you?(M)\n')
a = float(a)
print ('\n\n\n\n')

b = raw_input('Your computer son: How heavy are you?(KG)\n')

c = b/(a**2)
c = float(c//1)

print ('\n\n\n\n')
print ('Your computer son: But your BMI is',c)
print ('\n\n\n\n')

if c>=32:
	print ('Your computer son: Hey, daddy, please don\'t be too naive.') 

elif c>=28:
	print ('Your computer son: Hey, daddy, It\'s diffcult to find a girl you want.') 

elif c>=25:
	print ('Your computer son: Hey, daddy, You can find a girlfriend.') 

elif c>=18.5:
	print ('Your computer son: Hey, daddy, you will find a beautiful girlfriend you want.\nAnd then I will have a mommy.:)') 

else:
	print ('Your computer son: Hey, daddy, You can find a girlfriend.')

print ('\n\n\n\n')

