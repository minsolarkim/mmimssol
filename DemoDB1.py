# DemoDB1.py
#SQLite를 사용하는 데모 (로컬 데이터베이스)
import sqlite3 
#목수가 바닥에 장비를 내려놓고 시작 준비

#처음에는 데이터베이스파일(또는 메모리)를 생성
con = sqlite3.connect(":memory:")
#덮어쓰기가 안돼서 계속 임시 메모리에 만드는 약속(?)

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
# for row in cur:
#     print(row)

#1건 검색
print( cur.fetchone() )
#N건 검색
print("---fetchMany(2)---")
print( cur.fetchmany(2) )
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )

#결과를 슬라이싱
cur.execute("select * from PhoneBook;")
result = cur.fetchone()
print(result[0])
print(result[1])

#2차원 행열 데이터 [행][열]
print("---다중행의 경우---")
result = cur.fetchall()
print(result[0][0])
print(result[0][1])



