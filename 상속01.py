class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        # 이거 너무 중복되어있으니까
        
        # 명시적으로 부모클래스의 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__)
# print(s.__dict__)
#딕셔너리로 볼 수 있음

p.printInfo()
s.printInfo()


