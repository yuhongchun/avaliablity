def deco(func):
    def deco():
        print 'before func'
        func()
        print 'after func'
    return deco

@deco
def myfunc():
    print 'My function called,I am hongchun.yu'

myfunc()