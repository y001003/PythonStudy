
# print("Python","Java","JavaScript", sep=" vs ", end="?")
# print("무엇이 더 재미있을까요?")
# import sys
# print("Python","Java", file=sys.stdout)
# print("Python","Java", file=sys.stderr)

# dictionary
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():# items() : key와 value 쌍으로 보내줌
#     #print(subject,score)
#                 #왼쪽정렬 8공간     오른쪽 정렬 4개공간
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 무조건 String 문자열형태로 기억된다.
# print("입력하신 값은 " + answer + "입니다.")
