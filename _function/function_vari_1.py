# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")#end -> 이문장 다음에 줄바꿈을 하지 않음
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석",20,"Python","Java","C","C++","C#")
# profile("김태호",25,"Kotlin","Python","","","")
# 만약 사람이 늘어나면 ""을 계속 써야하나?
# 만약 유재석이 언어를 늘리면 함수를 바꾸어야하나? 딜레마
# -> 가변인자
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")#end -> 이문장 다음에 줄바꿈을 하지 않음
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"Python","Java","C","C++","C#","SQL")
profile("김태호",25,"Kotlin","Python")