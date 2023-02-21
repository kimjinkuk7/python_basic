# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해서 사용.

# 부모 클래스
class Monster():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"{self.name} 지상으로 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"{self.name} 날기")

wolf = Wolf("울프", 1000, 100)
wolf.move()

shark = Shark("상어", 800, 90)
shark.move()

dragon = Dragon("용", 8000, 1000)
dragon.move()