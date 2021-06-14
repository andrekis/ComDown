from termcolor import colored
from os import system, name


from tools.jsonedit import *


'''
def helloWorld():
    print(colored('Hello World!', 'green'))

def log(text, color='white'):
    print(colored(text, color))

def error(text):
    print(colored(text, 'red'))

def success(text):
    print(colored(text, 'green'))

def detail(text, color):
    print(colored(text, color))

def prog(total, remaining):
    main(colored('Downloading', 'green'))
    print(colored('\rImages: [','blue',attrs=['bold']),end='')
    for _ in range(0,int((total-remaining)/total*30)): print (colored(' ','white' ,'on_green'),end='')
    for _ in range(0,int(remaining/total*30)): print (colored('-', 'yellow'), end='')
    print(colored(']','blue',attrs=['bold']),end='')

def main(text=''):
    print(colored('Wellcome to ComDown','blue'),end='')
    if text!='':
        print(colored(f'Task: {text}'))
'''

def error(text):
    print(colored(text, 'red'))

def status(text, color= 'white'):
    obj= getdata()
    obj['status']= colored(text, color)
    setdata(obj)
    refresh()

def prog(total, downloaded, string):
    print(colored(f'{string}: [','blue',attrs=['bold']),end='')
    for _ in range(0,int(downloaded/total*30)): print (colored(' ','white' ,'on_green'),end='')
    for _ in range(0,int((total-downloaded)/total*30)): print (colored('-', 'yellow'), end='')
    print(colored('][', 'blue', attrs=['bold'])+colored(f'Downloaded: {str(downloaded)}/{str(total)}','green',attrs=['bold'])+colored(']', 'blue', attrs=['bold']),end='\n')

def refresh():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print(colored('Wellcome to ComDown', 'blue', attrs=['bold']), end='\n')
    obj= getdata()
    if 'title' in obj:
        print(colored('name: ', 'blue', attrs=['bold'])+obj['title'], end='\n')
    elif 'subtitle' in obj:
        print(colored('name: ', 'blue', attrs=['bold'])+obj['subtitle'], end='\n')
    if 'status' in obj:
        print(colored('Status: ', 'blue', attrs=['bold'])+obj['status'], end='\n')
    if 'total-series' in obj:
        prog(obj['total-series'], obj['downloaded-series'], 'chapter')
    if 'total-image' in obj:
        prog(obj['total-image'], obj['downloaded-image'], 'Image  ')
    if 'total-links' in obj:
        prog(obj['total-links'], obj['downloaded-links'], 'Links  ')
    if 'Error' in obj:
        print(colored(f"Error: {obj['Error']}", 'red'), end='\n')
    if 'print' in obj:
        print(obj['print'],end='\n')
    
    