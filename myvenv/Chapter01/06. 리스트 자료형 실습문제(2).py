a = []

x = int(input("1일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("2일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("3일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("4일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("5일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("6일차 턱걸이 횟수>>>"))
a.append(x)
x = int(input("7일차 턱걸이 횟수>>>"))
a.append(x)

print(a)

total = 0

for i in a:
    total += i

avg = total / len(a)
print(int(avg))