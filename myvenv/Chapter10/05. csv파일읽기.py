import csv

file = open("./myvenv/Chapter10/student.csv", "r", newline="", encoding="utf_8_sig")
reader = csv.reader(file)

for data in reader:
    print(data)

file.close()