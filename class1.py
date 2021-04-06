# class1.py
class Person:
    #클래스에 소속된 멤버면수(주로 데이터를 공유) static 키워드 추가
    num_person = 0
    def __init__(self):
        #인스턴스 멤버 변수는 여기에서 초기화
        self.name = "default name"
        Person.num_person += 1
        #이 안에 있으면 인스턴스고
    def print(self):
        print("My name is {0}".format(self.name))


#인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
print("인스턴스 갯수 : {0}".format(Person.num_person))

p1.print()
p2.print()
#따로 저장돼서 설계도면은 같은데 빨간지붕 파란지붕 이런식으로 따로 지어짐

#런타임시에 멤버 변수 추가(동적 언어도 가능~~) (말도 안되는 거임)
#디자인타임(코딩, 개발...)
Person.title = "new title"
print(Person.title)
print(p1.title)
print(p2.title)

