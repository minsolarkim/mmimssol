# DemoOS.py
from os.path import *
#이렇게 하면
# import os.path 보다 좋음?
 
# print( dir(os.path) )

print( abspath("python.exe") )
print( basename("c:\\python38\\python.exe"))
print( exists("c:\\python38\\python.exe"))
print( getsize("c:\\python38\\python.exe"))
#나중에 서버 구축하게 되면 많이 사용하게 될 것

#운영체제에 있는
from os import *
# c:\work2 --> c: 
print("현재 폴더:", getcwd() ) 
chdir("..")
chdir("c:\\work2")
print("현재 폴더: ", getcwd() )

#실행파일 실행 가능 한가요?
#외부에 실행파일 수행
# system("notepad.exe")

#파일, 폴더 리스트
import glob
print( glob.glob("*.py"))
print("=" * 20)
for item in glob.glob("*.*"):
    print(item)




