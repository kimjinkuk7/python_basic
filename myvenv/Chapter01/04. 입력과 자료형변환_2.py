from datetime import datetime

a = input("출생년도를 입력하세요 : ")

Tyear = datetime.today().year

year = Tyear - int(a)

print(year)