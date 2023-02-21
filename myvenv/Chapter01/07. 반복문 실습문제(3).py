krList = ["안녕", "반가워", "잘가", "메롱"]

totalCnt = len(krList)
successCnt = 0
failCnt = 0
for kr in krList:
    print("문제 : ", kr)
    x = input("답을 입력하세요 >>")

    if kr == x:
        successCnt += 1
    else:
        failCnt += 1

print("전제 문제 개수 : ", totalCnt, "개")
print("맞힌 문제 개수 : ", successCnt, "개")
print("틀린 문제 개수 : ", failCnt, "개")