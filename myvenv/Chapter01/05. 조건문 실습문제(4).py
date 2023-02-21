kr = int(input("국어>>"))
mt = int(input("수학>>"))
eg = int(input("영어>>"))

total = kr + mt + eg
avg = total / 3

if 0 <= kr <= 100 and 0 <= mt <= 100 and 0 <= eg <= 100 :
    if avg >= 80 :
        print ("불합격")
    else :
        print("합격")
else :
    print("잘못 입력하였습니다.")