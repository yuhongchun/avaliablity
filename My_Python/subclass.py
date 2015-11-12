# -*- coding: utf-8 -*-
# 这个例子比较好，能比较清楚的说明白python的继承和多态
class base(object):
    def __init__(self, name):
        self.name = name
    def printest(self):
        print "base class: ", self.name
 
class subclass1(base):
    def printest(self):
        print "sub class 1: ", self.name
         
class subclass2(base):
    def printestmy(self):
        print "sub class 2,hehe: ", self.name
    #即时subclass2中没有定义printest方法，但由于它是base类的子类，所以继续了其printest方法。
 
class subclass3(base):
    pass
 
def testFunc(obj):
    obj.printest()
 
 
if __name__ == "__main__":
    testFunc(subclass1("cc"))
    testFunc(subclass2("yhc"))
    testFunc(subclass3("tor"))

emp  = subclass2("yht")
emp.printestmy()
emp.printest()