#     # 패키지  모듈
# import travel.thailand
#         #패키지    모듈     클래스
# trip_to = travel.thailand.ThailandPackage()
#        # 메서드
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import * 
# *은 모든 것을 가지고 오는 것인데
# __init__ 에서 공개 범위를 설정해야 가능
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))