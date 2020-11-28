# 다른 사람이 만든 패키지 사용 활용
# pypi 사이트 
# 터미널에 아래 작성
# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list -> 가지고 있는 패키지 리스트 보여준다
# pip show beautifulsoup4 -> 특정 패키지에 대한 정보
# pip install --upgrage beautifulsoup4 -> 설치된 패키지 업데이트
# pip uninstall beautifulsoup4 -> 삭제