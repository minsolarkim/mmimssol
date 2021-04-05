# mutable and immutable.py
#복습
#가변형과 불변형(int, float, 복소수, 튜플, 문자열)
print("---가변형, 불변형---")

print("---불변형---")
a = 1.2
print( id(a) )
a = 2.3
print( id(a) )
#값이 아예 바뀜

print("---가변형---")
lst = ["red", "blue"]
print( id(lst) )
lst.append("white")
print( id(lst) )
#값이 바뀔 수 있으나 주소 안 바뀜

print("---전역변수, 지역변수---")
x = 5
def func(a):
    return a+x
    
def func2(a):
    x = 1
    return a+x

#호출
print( func(1) ) #a에 1을 넣은 거임!!!
print( func2(1))

