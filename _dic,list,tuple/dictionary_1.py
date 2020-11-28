        #  key:value
cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])

# 새로운 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)

# 손님 업데이트
cabinet["A-3"] = "정형돈"
print(cabinet)

# 간 손님 ( 삭제)
del cabinet["B-100"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key value 동시에 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear
print(cabinet)

# 재정의
cabinet = {1: "유재석",2:"정형돈"}
print(cabinet)

