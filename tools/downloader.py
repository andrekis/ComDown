import requests
import threading
import os

from tools.console import *
from tools.jsonedit import *

data={
	"links1":[],
	"downloaded1": "",
	"path1": "",
	"length": ""
}

# links1=[]
# downloaded1=0
# path1=''
# length=0
threads=[]

def download(links, path, downloaded=0, threadNum=1):
	sort(links)
	data['path1']=path
	data['length']=len(links)
	data['downloaded1']=downloaded
	check()
	status('downloading...', 'green')
	threadManage(threadNum)

def threadManage(threadNum):
	for _ in range(threadNum):
		t=threading.Thread(target=save)
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
	print('')


def sort(links):
	data['links1'].clear()
	for x in range(0,len(links)):
		temp={
			"link": links[x],
			"name": str(x+1)+links[x][links[x].rindex('.'): links[x].rindex('')]
		}
		data['links1'].append(temp)
		# print(links1)

def check():
	# for x in data['links1']:
	# 	path= os.path.join(data['path1'], x['name'])
	# 	if os.path.isfile(path):
	# 		# print ("File is exist")
	# 		data['links1'].remove(x)
	# 		print(data['links1'])
	arr=[]
	for x in data['links1']:
		if not(os.path.isfile(os.path.join(data['path1'], x['name']))):
			arr.append(x)
	data['links1']=arr.copy()
	arr.clear()

def save():
	# for obj in data['links1']:
	if len(data['links1']) != 0:
		# try:
		# 	link=data['links1'][0]['link']
		# 	path= os.path.join(data['path1'], data['links1'][0]['name'])
		# 	r = requests.get(link, allow_redirects=True)
		# 	data['links1'].pop(0)
		# 	open(path, 'wb').write(r.content)
		# except:
		# 	print(colored('\rfailed trying again...', 'red'))
		
		# getting current link
		temp=data['links1'][0]
		data['links1'].pop(0)
		link=temp['link']
		path= os.path.join(data['path1'], temp['name'])
		try:
			r = requests.get(link, allow_redirects=True, timeout=180)
			open(path, 'wb').write(r.content)
			obj=getdata()
			obj['total-image']=data['length']
			obj['downloaded-image']=data['length']-len(data['links1'])
			setdata(obj)
			refresh()
		except:
			data['links1'].insert(0, temp)
			obj=getdata()
			try:
				obj['Error']=int(obj['Error'])+1
				setdata(obj)
				refresh()
			except:
				obj['Error']=1
				setdata(obj)
				refresh()


		#loading bar
		# print(colored('\r[','blue',attrs=['bold']),end='')
		# for _ in range(0,int((data['length']-len(data['links1']))/data['length']*30)): print (colored(' ','white' ,'on_green'),end='')
		# for _ in range(0,int(len(data['links1'])/data['length']*30)): print (colored('-', 'yellow'), end='')
		# print(colored(']','blue',attrs=['bold']),end='')
		# prog(data['length'], len(data['links1']))
		#/loading bar
		#updating image downloading value

		# //
		# print(colored(f"[Downloaded {data['length']-len(data['links1'])}/{data['length']}]", 'green', attrs=['bold']), end='')
		save()

	# else:
	# 	print(colored('Download compeleted','green'),end='')
