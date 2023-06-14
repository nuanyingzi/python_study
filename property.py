# 使用@property
import datetime_demo


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0~100')
        self._score = value


s = Student()
s.score = 99
print(s.score)


class Person(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be an integer!')
        if value < 0:
            raise ValueError('birth must be bigger than 0')
        self._birth = value

    @property
    def age(self):
        return datetime.datetime.now().year - self._birth


p = Person()
p.birth = 1999
print(p.age)


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('Width must be an number')
        if value <= 0:
            raise ValueError('Width must be greater than 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Height must be an number')
        if value <= 0:
            raise ValueError('Height must be greater than 0')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')