# pip install -U Flask

#Flask :캐멀케이즈 = 클래스
from flask import Flask

app = Flask(__name__)


@app.route("/")  # 데코레이터
def hello():
    return "Hello, world! <h1>안녕하세요</h1>"


# 사용하기
"""
$ set FLASK_APP=파일이름.py  
    #환경변수 설정(터미널에서 한번만 실행)
$ flask run     #flask 명령 
"""

# 라이브러리: 정상적인 제어방법으로 사용하는 모듈
# 프레임워크: 제어역전(IoC)이 일어나는 모듈

# 정상적인 제어= 개발자가 모듈을 직접 사용
# 제어역전(Inversion of Control) = 모듈이 개발자의 코드를 사용

'''
-> flask run이라는 명령어를 사용했을 뿐인데 @app.route로 가서 hello()라는 함수를 실행해서 그 값을 리턴한것 뿐이다. 
'''
