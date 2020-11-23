#Continue 이후에 이어지는 것X 다음반복으로 진행

absent = [2 , 5] # 결석
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}번아, 책을 읽어라".format(student))

