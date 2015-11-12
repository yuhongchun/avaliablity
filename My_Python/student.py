class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an int,This is an error")
        if value < 0 or value > 100:
            raise ValueError("score must between 0-100")
        self._score = value

s = Student()
s.score = -2.8
print s.score 
