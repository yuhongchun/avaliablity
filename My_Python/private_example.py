class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print "%s: %s" % (self.__name, self.__score)
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score

bart = Student("Bart Simpson", 96)
# Student.set_score('45')
# Student.set_score(44)
print Student.get_score(bart)
print Student.get_name(bart)

