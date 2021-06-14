f= open('./links.txt', 'r')

def check(code):
    try:
        eval(code)
        return True
    except:
        return False
    



for x in f:
    if check("x[x.index(''):x.rindex(',')]"):
        print(x[x.index(''):x.rindex(',')])
    else:
        if not x.endswith('\n'):
            print(x[x.index(''):x.rindex('')])
        else:
            print(x[x.index(''):x.rindex('')-1])