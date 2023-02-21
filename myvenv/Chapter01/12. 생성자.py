# 생성자
# 인스턴스를 만들때 호출되는 매서드

from pkg_resources import declare_namespace


class Monster():
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health

goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

wolf = Monster(1500, 200, 350)
wolf.decrease_health(200)
print(wolf.get_health())