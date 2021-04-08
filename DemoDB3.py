# DemoDB3.py
# DemoDB2.py
#SQLite를 사용하는 데모 (로컬 데이터베이스)
import sqlite3 
#목수가 바닥에 장비를 내려놓고 시작 준비

#처음에는 데이터베이스파일(또는 메모리)를 생성
con = sqlite3.connect(":memory:")
#덮어쓰기가 안돼서 계속 임시 메모리에 만드는 약속(?)

# con = sqlite3.connect("c:\\work2\\sample2.db")
#test.db했는데 안돼서 sample로 바꿈


#SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()

#저장소(테이블)을 만들기 : 테이블 스키마(뼈대를 만드는 거임) (데이터 구조화)
cur.execute("create table PhoneBook (Name text, PhoneNum test);")

#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

#입력 파라메터 처리(python format {0},{1})
#텍스트박스(GUI, Web Page)에서 입력을 받아서 처리

name = "ona"
phoneNumber = "010-999"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#다중의 레코드(행, row)를 입력받는 경우 : 2차원 행열데이터
datalist = (("tom", "010-123"), ("dsp", "010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#이 때 executemany를 사용하는 구만!!

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#백업받기(덤프)
#파일로 저장(Write Text)
f = open("c:\\work2\\dump.sql", "wt")
for item in con.iterdump():
    print(item)
    f.write(item + "\n")

f.close()

#복구하기(with 블럭 안에서 파일을 닫고 빠져나온다.)
with open("c:\\work2\\dump.sql") as f:
    SQLScript = f.read()
#구문을 실행하기 위해
con = sqlite3.connect("c:\\work2\\Demo5.db")
cur = con.cursor()
#다중 라인으로 된 SQL배치파일
cur.executescript(SQLScript)
con.close()