# hexdump 설치

# 1. 컴퓨터가 데이터를 저장할 때는 무조건 숫자로 저장한다.
# 2. 파이썬의 파일 구분: 텍스트 데이터와 바이너리 데이터

# 텍스트 데이터: 텍스트 편집기 편집 가능
file = open("55강_텍스트데이터와_바이터리데이터.py", "r")
print(file.open())
file.close()

# 바이너리 데이터: 텍스트 편집기 편집 불가능
# > 전용 편집기를 사용하여 편집
# > 이미지, 오디오, 폰트
# data 를 읽을려고 하면 오류가 발생함
# rb = read bytes
# binary : 이진수
# bit : 이진수로 표현된 데이터 하나
# byte = bite * 8

file = open("font.woff2", "rb")
data = file.read()
print(data[:100])
file.close()
# 결과값으로 앞에 b가 붙여져서 나온 문자열을 바이트 스트링이라 함

# 3. 텍스트 데이터를 읽고 쓰는 방법
# 4. 바이너리 데이터를 읽고 쓰는 방법
