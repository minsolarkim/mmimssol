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

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)