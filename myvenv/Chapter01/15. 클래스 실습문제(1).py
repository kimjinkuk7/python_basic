class Item():
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}] 입니다.")

    def discard(self):
        if self.isdropable :
            print(f"[{self.name}] 아이템을 버렸습니다.")
        else :
            print(f"[{self.name}] 아이템을 버릴 수 없습니다.")

class Wearableitem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        print(f"[{self.name}]을 착용했습니다. {self.effect}")

class Usableitem(Wearableitem):
    def use(self):
        print(f"[{self.name}] 아이템을 사용했습니다. {self.effect}")


# 인스턴스 생성
sword = Wearableitem("장검", 1000, 80, True, "반짝임")
sword.wear()
sword.sale()
sword.discard()

potion = Usableitem("빨간물약", 300, 0.1, False, "체력 200증가")
potion.discard()
potion.sale()
potion.use() 