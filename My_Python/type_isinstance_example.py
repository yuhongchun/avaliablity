class test1:
    print "hello world"
class test2(test1):
    pass

if __name__=="__main__":
    x=123
    print type(x)
    y=123.1
    print type(y)
    print
    z1=test1()
    z1
    print(type(z1))
    z2=test2()
    z2
    print(type(z2))
    print
    z3='sdf'
    print(type(z3))
    j1=True
    print(type(j1))
    j2=['s']
    print(type(j2))
    print 
    j3=('sdf')
    print type(j3)
    j4={'sdf':132}
    print type(j4)

print isinstance('a',str)
print isinstance({'sdf':132},dict)
print isinstance(['s'],list)
print isinstance((1,),tuple)
