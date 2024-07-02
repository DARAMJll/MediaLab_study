import math
import random
import os
import datetime

print(math.log10(100))
print(math.cos(0))
print(math.pi)

print(random.random())

print(os.getlogin())
print(os.getcwd())

pi_day = datetime.datetime(2024, 7, 2, 16, 52, 00)

today = datetime.datetime.now()
print(today.strftime("%Am %B %dth %Y"))

name = input("이름을 입력하세요 : ")
print(name)

x = int(input("숫자를 입력하세요"))
print(x + 10)