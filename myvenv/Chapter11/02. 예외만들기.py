# raise 구문을 사용하여 강제로 에러만들기

num = int(input("음수를 입력해 주세요>>>"))

if num >= 0 :
    raise Exception("양수는 입력 불가")