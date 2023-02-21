# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해서 사용.

import random

# 클래스 변수
# 인스턴스들이 모두 공유하는 변수

# 부모 클래스
class Monster():
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1    # 클래스변수 (모두가 공유되는..)

    def move(self):
        print(f"{self.name} 지상으로 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)  # 부모클래스에 인자를 다 가져온다.
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print(f"{self.name} 날기")

    def skill(self):
        print(f"{self.name} 스킬 사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프", 1000, 100)
wolf.move()
print(wolf.max_num)

shark = Shark("상어", 800, 90)
shark.move()
print(shark.max_num)

dragon = Dragon("용", 8000, 1000)
dragon.move()
dragon.skill()
print(dragon.max_num)