#일반 유닛
class Unit: # 부모 class
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))
    def move(self, location):
        print("[지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

#공격 유닛
class AttackUnit(Unit): # 자식 class
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    # method
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다."\
            .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 남은 체력은 {1} 입니다."\
            .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 수송기, 공격 X, 공중유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
#공격 유닛, 공중유닛 다중 상속
class FlayableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    # 메서드 오버라이딩 move로 fly 기동하도록 메서드 move 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

# 배틀크루저 : 공중 유닛, 체력, 공격력 좋지만 느림
battlecruiser = FlayableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")

