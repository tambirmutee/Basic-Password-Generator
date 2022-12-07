from random import *

passLength = int(input("Enter the password length: "))
number = '0123456789'
lower_case = 'qwertyuopilkjhgfdsazxcvbnm'
upper_case = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
symbol = '@>£#$½§{[]}\|~!^+%&/()=?_-*'
randomize = number+lower_case+upper_case+symbol
password = ''.join(sample(randomize,passLength))
print(password)