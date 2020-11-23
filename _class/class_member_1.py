# 멤버변수 : 클래스 내에서 정의된 변수 name, hp, damage

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage =damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
#wraith2에 clocking 이라는 변수를 추가로 할당한 것
wraith2.clocking = True 

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# wraith1에는 clocking 이라는 변수가 없어 에러발생.
# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))
