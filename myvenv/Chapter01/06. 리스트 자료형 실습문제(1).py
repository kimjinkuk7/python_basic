from imp import release_lock


reslut = [33, 40, 12, 63, 52]

reslut.append(9)
print(reslut)

reslut[1] = 50
print(reslut)

print(reslut[2:])

reslut.sort()
print(reslut)