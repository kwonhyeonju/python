# 정사각형 만들기
# 문제점1 : 사용자가 양수값외 다른값들을 넣을 수 있음!!
# 해결1 : 예외 활용


class Rect:
    def __init__(self, width, height):
        # 해결1
        if width <= 0 or height <= 0:
            raise Exception("너비와 높이는 음수가 아닙니다.")

        '''문제점2
        self.width = width
        self.height = height
        '''
        self.__width = width
        self.__height = height
    '''
    #해결3    
    def get_width(self):
        return self.__width
    def set_width(self, width):
        if width <= 0 :
            raise Exception("너비는 음수가 아닙니다.")
        self.__width = width

    def get_height(self):
        return self.__height
    def set_height(self, height):
        if height <= 0:
            raise Exception("높이는 음수가 아닙니다.")
        self.__height = height
    '''

    # 해결4 :
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise Exception("너비는 음수가 아닙니다.")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def set_height(self, height):
        if height <= 0:
            raise Exception("높이는 음수가 아닙니다.")
        self.__height = height

    def get_area(self):
        '''문제점2
        return self.width * self.height
        '''
        return self.__width * self.__height


rect = Rect(10, 10)
# 문제점2: 사용자가 직접 지정해주는경우!(음수값으로)
# 해결2: 프라이빗 변수를 활용 (__width, __height)
'''문제점2
rect.width = -10
'''
rect.__width = -10
# 문제점3 :
# print(rect.__width)
# 를 하면 값을 불러올 수 없음(변경을 아예 못함)
# 해결3 : 겟터 셋터 활용

# 문제점4 :
# 너비에 10을 더한값을 사용할려고 할때
# rect.set_width(rect.get_width()+10)
# 요것이 개떡 같음
# 해결4 :프로퍼티사용(숫자계산처럼 사용가능)
rect.width += 10
print(rect.get_area())
