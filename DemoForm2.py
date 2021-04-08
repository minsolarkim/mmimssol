# 두번째 화면




# 화면단(DemoForm.ui) + 로직단(DemoForm.py)
import sys
#Qt패키지 로딩: 패키지명.모듈명
from PyQt5.QtWidgets import *
from PyQt5 import uic

#미리 만든 화면을 로딩 (두번째 화면)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#같은 타입이 우선?

#다이알로그를 상속받아서 폼클래스를 정의
class DemoForm(QMainWindow, form_class): #QDialog아니고 
                #ㄴ대화상자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #시그널(이벤트)를 처리하는 슬롯메서드
    def firstClick(self): # 오타 주의!!
        self.label.setText("첫번째 클릭")
    def secondClick(self):
        self.label.setText("두번째 클릭")
    def thirdClick(self):
        self.label.setText("세번째 클릭")

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