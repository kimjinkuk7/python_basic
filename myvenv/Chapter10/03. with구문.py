# with ������ ����ϸ� �ڵ� file close ���ش�.
with open("./myvenv/Chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data) 