# err.py
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'THis is an Error!'
        raise

def main():
    # print foo('0')
    print bar('0')

main()
