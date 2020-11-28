# __init__ : 파이썬에서 사용되는 생성자
# 마린, 탱크 등 클래스로부터 만들어지는 객체가 만들어질때 자동적으로 생성됨
# 멤버변수 : 클래스 내에서 정의된 변수 name, hp, damage

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage =damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
