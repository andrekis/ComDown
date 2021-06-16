import requests
from bs4 import BeautifulSoup

from tools.console import *
from tools.jsonedit import *

temp=[]

def generate(link):
	isLoaded=False
	temp.clear()
	# loading page
	status('Fetching page', 'yellow')
	# //
	try:
		page=requests.get(link)
		isLoaded=True
		# page loaded
		status('Page Loaded', 'green')
		# //
	except IOError:
		error(IOError)
		error('Failed to load the page. Make sure you have active connection and you can visit the webpage.\nIf the problem still remain then report the error.')
	if(isLoaded):
		page=page.content
		soup=BeautifulSoup(page,'html.parser')
		title=soup.title.string
		title=title[title.index('-')+1: title.rindex('All')-3]
		if '|' in title:
			title= title[0: title.rindex('|')]+'-'+title[title.rindex('|')+1:title.rindex('')]
		# saving title
		obj= getdata()
		obj['subtitle']= colored(title, 'yellow')
		setdata(obj)
		refresh()
		# //
		status('scrapping', 'blue')
		for img in soup.find_all('div', class_='page-break'):
			img=img.contents[1]
			try:
				temp.append(img.get('data-src')[img.get('data-src').index('h'): img.get('data-src').rindex('?')])
			except:
				temp.append(img.get('data-src')[img.get('data-src').index('h'): img.get('data-src').rindex('')])
		links=[title, temp]
		return links



def chapGenerate(link):
	isLoaded=False
	try:
		# loading page
		status('Fetching page', 'yellow')
		# //
		page=requests.get(link)
		isLoaded=True
		# page loaded
		status('Page Loaded', 'green')
		# //
	except IOError:
		error(IOError)
		error('Failed to load the page. Make sure you have active connection and you can visit the webpage.\nIf the problem still remain then report the error.')
	if(isLoaded):
		page=page.content
		soup=BeautifulSoup(page, 'html.parser')
		title=soup.title.string
		title=title[title.index(''): title.rindex('Porn Comic')]
		if '|' in title:
			title= title[0: title.rindex('|')]+'-'+title[title.rindex('|')+1:title.rindex('')]
		# saving title
		obj= getdata()
		obj['title']=colored(title, 'yellow')
		setdata(obj)
		# //
		# print(soup.find_all('li', class_='wp-manga-chapter')[0].contents[1]['href'])
		links=[]
		status('scrapping', 'blue')
		for li in soup.find_all('li', class_='wp-manga-chapter'):
			links.append(li.contents[1]['href'])
		links.reverse()
		temp=[title, links]
		return temp