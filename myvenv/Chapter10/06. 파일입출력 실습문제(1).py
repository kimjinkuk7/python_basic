import csv

#data = [
#    ["종목", "매입가", "수량", "목표가"]
#    , ["삼성전자", 85000, 10, 90000]
#    , ["NAVER", 380000, 5, 400000]
#]

#file = open("./myvenv/Chapter10/mustock.csv", "w", newline="", encoding="utf_8_sig")
#w = csv.writer(file)
#for i in data:
#    w.writerow(i)
#file.close()

def show_profit(data):
    name = data[0] # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount
    profit_ratio = (target_price / purchase_price - 1) * 100

    print(f"{name} {profit} {profit_ratio:.2f}%")

file = open("./myvenv/Chapter10/mustock.csv", "r", newline="", encoding="utf_8_sig")
r = list(csv.reader(file))

for i in r[1:]:
    show_profit(i)

file.close()