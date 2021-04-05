# web1.py
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("c:\\work2\\test01.html", "rt",encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
# print( soup.prettify() )

# <p>를 모두 검색해~ (리스트형식으로 리턴)
# print(soup.find_all("p"))

#첫번째 <p>를 검색
# print( soup.find("p"))

#<p class="outer-text"> 된 경우(약간의 필터링)
print ( soup.find_all("p", class_="outer-text") )
#find랑 find_all 차이 있다
#언더바 약간 눈에 거슬림?  - 이거 왜 쓰냐! class는 파이썬의 키워드임. 그래서 매개변수명이나 변수로 사용하면 안됨. 이름충돌 면하려고 언더바 붙임.

#특정 id속성을 검색
# print( soup.find(id="first") )

#<a> 태그 가져와
print( soup.find_all("a") )
print( soup.find_all("b") )

#태그를 제거하고 내부 문자열(컨텐츠만)
#<p> 컨텐츠</p>
for tag in soup.find_all("p"):
    #앞뒤에 공백문자를 제거
    print( tag.text.strip() )

    





