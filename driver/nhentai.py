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
	    title=soup.find('span', class_='pretty').getText()
        # getting total image number
	    total=len(soup.findAll('div', class_='thumb-container'))

    # going to the first image page
    firstImg='https://nhentai.net'+soup.find('a', class_='gallerythumb').get('href')
    try:
        # loading page
        status('Fetching page', 'yellow')
        # //
        page=requests.get(firstImg)
        isLoaded=True
        # page loaded
        status('Page Loaded', 'green')
        # //
    except IOError:
        error(IOError)
        error('Failed to load the page. Make sure you have active connection and you can visit the webpage.\nIf the problem still remain then report the error.')
    if (isLoaded==True):
        page=page.content
        soup= BeautifulSoup(page, 'html.parser')
        # getting the first image link
        firstImgLink=soup.find('section', id='image-container').contents[0].contents[0].get('src')
        # predicting all the image links
        for x in range(0, total, 1):
            temp.append(firstImgLink[0: firstImgLink.rindex('/')+1]+str(x+1)+'.jpg')
        links=[title, temp]
        return links



