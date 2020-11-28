python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index +1) # 처음 n을 찾은 다음열부터 찾기 시작
print(index)

print(python.find("Amazing"))
print(python.find("Java"))
#print(python.index("Java"))
print(python.count("n"))
