from tools.console import *
import requests
from bs4 import BeautifulSoup

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
		title= soup.find(id="page-title").string[soup.find(id="page-title").string.index('')+1:soup.find(id="page-title").string.rindex('')]
		# saving title
		obj= getdata()
		obj['subtitle']= colored(title, 'yellow')
		setdata(obj)
		refresh()
		# //
		for p in soup.find_all('p', class_='jb-image'):
			try:
				temp.append(p.contents[0]['src'][p.contents[0]['src'].index(''): p.contents[0]['src'].index('styles')]+p.contents[0]['src'][p.contents[0]['src'].index('comics'): p.contents[0]['src'].rindex('?')])
			except:
				temp.append(p.contents[0]['src'][p.contents[0]['src'].index(''): p.contents[0]['src'].index('styles')]+p.contents[0]['src'][p.contents[0]['src'].index('comics'): p.contents[0]['src'].rindex('')])
		links=[title, temp]
		return links





# for img in soup.find_all('div', class_='jb-bb-btn-download'):
# 	try:
# 		temp.append(img.get('data-src')[img.get('data-src').index('h'): img.get('data-src').rindex('?')])
# 	except:
# 		temp.append(img.get('data-src')[img.get('data-src').index('h'): img.get('data-src').rindex('')])
# links=[title, temp]
# return links