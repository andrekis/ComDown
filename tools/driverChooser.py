from tools.console import *
import driver.allPornComic as allPornComic
import driver.azPornComics as azPornComics
import driver.multPorn as multPorn
import driver.nhentai as nhentai


def choose(link, chapDown=False):
	if ('allporncomic' in link):
		if(chapDown==False):
			links=allPornComic.generate(link)
		else:
			links=allPornComic.chapGenerate(link)
		return links
	elif('multporn.net' in link):
		if(chapDown==False):
			links= multPorn.generate(link)
			return links
		else:
			error('chapdown not supported for this website.')
	elif('azporncomics.com' in link):
		if(chapDown==False):
			links= azPornComics.generate(link)
			return links
		else:
			error('chapdown not supported for this website.')
	elif('nhentai.net' in link):
		if(chapDown==False):
			links= nhentai.generate(link)
			return links
		else:
			error('chapdown not supported for this website.')
	else:
		error('Webpage not supported.\nNotify me; in git to get the webpage support')