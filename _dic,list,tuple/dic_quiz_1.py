# Quiz 댓글 이벤트 열기
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰
# 추천 프로그램 작성

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample 을 활용

from random import *

# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,2))


# replier = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
replier = range(1,21) #1부터 20까지 숫자를 생성
replier = list(replier)
shuffle(replier)
print(replier)

winners = sample(replier, 4) #4명 중에서 1명은 치킨,3명은 커피
print(type(winners))

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))

# #치킨
# chicken = sample(replier,1)
# replier = set(replier)
# replier.remove(chicken)

# #커피
# coffee = sample(replier,3)

# print(chicken)
# print(coffee)


# chicken = int(random()*20)+1
# print(chicken)

# replier.remove(chicken)

# # 커피
# coffee = {0,0,0}
# coffee = list(coffee)
# i = random()*len(replier)
# coffee.update(0,(replier[i])
# replier.remove(replier[i])

# i = random()*len(replier)
# coffee.add(replier[i])
# replier.remove(replier[i])

# i = random()*len(replier)
# coffee.add(replier[i])
# replier.remove(replier[i])

# print(chicken, coffee)
# print(replier)
