#encoding:utf-8
import time

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        time.sleep(3)
        end = time.clock()
        # print '程序开始时间:',start
        # print '程序结束时间:',end
        print '程序运行时间:',end-start

    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()