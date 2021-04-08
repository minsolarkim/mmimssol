# 세번째 화면

# 화면단(DemoForm3.ui) + 로직단(DemoForm3.py)
import sys
#Qt패키지 로딩: 패키지명.모듈명
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버에 요청
import urllib.request
#크롤링에 필요
from bs4 import BeautifulSoup
#ㄴ이거 web2.py에서 가져옴 !!! 두 줄 


#미리 만든 화면을 로딩 (두번째 화면)
form_class = uic.loadUiType("DemoForm3.ui")[0]
#같은 타입이 우선?

#다이알로그를 상속받아서 폼클래스를 정의
class DemoForm(QMainWindow, form_class): #QDialog아니고 
                #ㄴ대화상자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #시그널(이벤트)를 처리하는 슬롯메서드
    def firstClick(self): # 오타 주의!!
        data = urllib.request.urlopen('https://comic.naver.com/webtoon/list.nhn?titleId=20853&amp;weekday=fri')
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all("td", class_="title")
        f = open("c:\\work2\\webtoon.txt", "wt",encoding = "utf-8")
        #한글이 들어갔으니까 인코딩 지정해줘야 안 깨짐
        for item in cartoons:
            title = item.find("a").text
            print(title)
            f.write(title.strip() + "\n")
        f.close() #까먹으면 안됨!
        #이것도 web2.py에서 가져와서 필요한 부분만 자름
        #줄맞춤 주의!!!!!!!!!!!!

#직접 이 모듈을 실행했는지 진입점(Entry Point) 체크
if __name__ == "__main__":
    #실행 프로세스를 실행(python.exe)
    app = QApplication(sys.argv)
    #위에 있는 클래스의 인스턴스를 생성
    demoWindow = DemoForm()
    #창을 보여달라~~
    demoWindow.show()
    #지속적으로 실행
    app.exec_()
#이게 다 진입 절!!

#창이 뜬다 신기신기