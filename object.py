class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_student(self):
        print("name: %s, score: %d" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student("Tom", 99)
bart.print_student()
print(bart.get_grade())
