# 161
# 클래스는 틀이고 인스턴스는 객체

# 162
# class Human

# 163


class Human:
    pass


areum = Human()

# 164


class Human:
    def __init__(self):
        print("응애응애")


areum = Human()

# 165


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


areum = Human("아름", 25, "여자")

# 166


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


areum = Human("아름", 25, "여자")
print(areum.age)

# 167


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))


areum = Human("아름", 25, "여자")
areum.who()
