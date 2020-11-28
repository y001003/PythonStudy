# Quiz) 당신은 Cocoa 서비스를 이용하는 택시기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수
# 조건2 : 당신은 소요 시간 5분 ~15분 사이의 승객만 매칭

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 :16분)

# 총 탑승 승객 : 2 분
#---------------------------------------------
# 정답
# from random import *
# cnt = 0 #총 탑승 승객 수
# for i in range(1,51) : # 1~50 이라는 승객 수
#     time = randrange(5, 51) # 5분 ~50분 랜덤 소요 시간
#     if 5<= time <=15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 고객수 : {0}명".format(cnt))

#----------------------------------------------
from random import *

count = 1
match = 0

for i in range(1,51) :
    customer = randint(5,50)
    if customer >=5 and customer <=15:
        print("[0]"+str(count)+"번째 손님 (소요시간 : {0}분)".format(customer))
        count += 1
        match += 1
    else:
        print("[ ]"+str(count)+"번째 손님 (소요시간 : {0}분)".format(customer))
        count += 1
    

print("총 탑승 고객수 : {0}명".format(match))


