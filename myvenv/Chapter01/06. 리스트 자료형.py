animals = ["가물치", "벼메뚜기", "비단뱀", "도룡뇽"]

empty = []

print(animals[0])
print(animals[-1])

animals.append("고라니")
print(animals)

animals[1] = "청개구리"
print(animals)

del animals[0]
print(animals)

print(animals[1:3])
print(animals[:]) # 전체
print(animals[1:])
print(animals[:3])

animals.sort()
print(animals)

animals.sort(reverse=True)
print(animals)