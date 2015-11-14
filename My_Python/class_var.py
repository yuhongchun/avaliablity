#encoding:utf-8
#此实例说明类变量跟实例变量的区别。
class Test(object):
    num_of_instance = 0
    def __init__(self, name):
        self.name = name
        self.color = 'red'
        Test.num_of_instance += 1

if __name__ == '__main__':
    print Test.num_of_instance
    t1 = Test('jack')
    print Test.num_of_instance
    t2 = Test('lucy')
    t3 = Test('yhc')
    print t1.name , t1.num_of_instance,t1.color
    print t2.name , t2.num_of_instance,t2.color
