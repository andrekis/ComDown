def check(code):
    try:
        eval(code)
        return True
    except:
        return False
    

def extract(textPath):
    links=[]
    f= open(textPath, 'r')
    for x in f:
        if check("x[x.index(''):x.rindex(',')]"):
            links.append(x[x.index(''):x.rindex(',')])
        else:
            if not x.endswith('\n'):
                links.append(x[x.index(''):x.rindex('')])
            else:
                links.append(x[x.index(''):x.rindex('')-1])
    if links !=[]:
        return links
    f.close()