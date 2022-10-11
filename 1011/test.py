import re

x = '1*2+3-5'
print(re.split(['*','+'], x))