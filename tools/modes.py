import os
import json

from tools.driverChooser import *
import tools.downloader as downloader
from tools.pathBuild import *
from tools.console import *
from tools.jsonedit import *
from tools.linkExtractor import extract



def singleMode(data):
	link= data['link']
	path= data['path']
	downloaded= int(data['downloaded'])
	thread= int(data['thread'])

	if(link!=''):
		#scrapping all the images links
		links=choose(link)
		#creating downloader path
		path = build(links[0], path)	
		num= len(links[1])
		status('Starting Download','green')
		downloader.download(links[1], path,downloaded, thread)
	else:
		error('Link field is empty. Please input the link')


def multiMode(data):
	downloaded=0
	path= data['path']
	thread= data['thread']
	links= extract(data['textPath'])
	# saving total length of the links to json file
	obj=getdata()
	obj['total-links']=len(links)
	setdata(obj)
	for lin in range(downloaded, len(links)):
		if links[lin]!='':
			data['link']=links[lin]
			# updating chapdownloaded value
			obj=getdata()
			obj['downloaded-links']=lin
			setdata(obj)
			refresh()
			singleMode(data)
		if lin==len(links)-1:
			obj=getdata()
			obj['downloaded-links']=lin+1
			setdata(obj)
			refresh()
	
	status('All the comics are downloaded', 'green')			


def chapMode(data):
	data=data
	link= data['link']
	path= data['path']
	chapDownloaded= data['chapter']-1
	if (link!=''):
		#scrapping chapter links
		links=choose(link, True)
		#creating downloaded path
		path = build(links[0], path)
		data['path']=path
		num=len(links[1])
		# reading data from json file
		obj=getdata()
		# saving data to json file
		obj['total-series']=num
		setdata(obj)
		for lin in range(chapDownloaded, len(links[1])):
			data['link']=links[1][lin]
			# updating chapdownloaded value
			obj=getdata()
			obj['downloaded-series']=lin
			setdata(obj)
			refresh()
			# using single mode method
			singleMode(data)
			if lin==len(links[1])-1:
				obj=getdata()
				obj['downloaded-series']=lin+1
				setdata(obj)
				refresh()
		# status('Series download complete', 'green')