# DemoFunction2.py
#가변인자로 덧셈처리
def varAdd(*ar): # *ar은 튜플이고.. 뒤에꺼 들어갈 수 있다?!
    result = 0
    for item in ar:
        result += item

    return result

#호출
print( varAdd(2,3) )
print( varAdd(2,3,4))

#함수를 정의(단일값, 스칼라라고 함)
def add10(i):
    return i+10

x = [1,2,3,4,5]
#각 아이템에 맴핑하는 함수
for item in map(add10, x): #10씩 더해져서 [11,12,13,14,15] 이렇게 뜸
    print(item)

print("---람다함수사용---")
for item in map(lambda x:x+10, x):
    print(item)


#두 개가 결과는 똑같은데 둘 중에 더 간편한건 람다임!!