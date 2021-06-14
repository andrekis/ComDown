import json

def getdata():
    f= open('./tools/appdata.json', 'r')
    obj= json.load(f)
    f.close()
    return obj

def setdata(obj):
    with open('./tools/appdata.json', 'w') as f:
        json.dump(obj, f)
        f.close()
        
    