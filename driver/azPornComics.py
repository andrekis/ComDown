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
		title=title[title.index(''): title.index(',')]
		# saving title
		obj= getdata()
		obj['subtitle']= colored(title, 'yellow')
		setdata(obj)
		refresh()
		# //
		status('scrapping', 'blue')
		for div in soup.find_all('div', class_='picpagelink'):
			temp.append(div.contents[0]['href'])
		links=[title, temp]
		return links