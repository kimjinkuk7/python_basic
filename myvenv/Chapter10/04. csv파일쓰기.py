import csv
from encodings import utf_8_sig
data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8], 
    ["형돈", 5, 32]
]

file = open("./myvenv/Chapter10/student.csv", "w", newline="", encoding="utf_8_sig")
writer = csv.writer(file)

for i in data:
    writer.writerow(i)

file.close()