# 원화를 입력, 환율 입력 -> 달러값

from typing import final


won = input("원화금액을 입력하세요 >>>")
dollar = input("환율을 입력 하세요 >>>")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as ve: # 예외가 발생했을때 실행
    print("예외가 발생")
    print(ve)
except ZeroDivisionError as ze:
    print("0으로 나누기")
    print(ze)
else :
    print(int(won) / int(dollar))
finally:
    print("무조건실행")
