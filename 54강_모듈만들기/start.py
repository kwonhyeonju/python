# 코드를 시작하는 (파이썬 명령어를 입력하는 진입점)
import my_module
print(__name__)
# 내가 어떤 파일에 있는지 알수 있게 해줌
# python 파일.py
# 파일 > 모듈 > 모듈 > 모듈
# 파일 : 진입점(엔트리포인트)
# 메인 파일(main)
'''
같은 파일에 위치하면 바로 부를수 있음
다른 폴더에 있다면 
import 폴더/폴더/파일
'''
print(my_module.a)
print(my_module.b)
print(my_module.c())
if __name__ == "__main__":
    print("엔트리 포인트입니다.A")
