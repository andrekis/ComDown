from tools.console import *
import json
import sys 
sys.path.insert(1, '../')

#syncing with txt
'''
class data:
	workingMode= None
	link= None
	path= None
	downloaded= None
	textPath= None
'''
def sync():
    try:
        f = open('option.txt', 'rt')
        text=f.read()
        text=json.loads(text)
        return text
    except IOError:
        error('File not found creating new one')
        try:
            f= open('option.txt', 'x')
        except:
            error("Can't create file, permission may be denied")
        f= open('option.txt', 'w')
        text= '''{\n"comment":"ComDown",\n\n\n"comment_2":"1.Single Link 2.Multi Link(txt path require, each line will be considered as a link) 3.ChapterLink",\n"workingMode":"1",\n"downloaded":"0",\n"thread": "1",\n"link": "",\n"path": "",\n"textPath":""\n}'''
        f.write(text)
        success('File created successfully')
    finally:
        f.close()
	   	
	   	