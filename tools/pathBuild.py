from termcolor import colored
import os


def build(title, path):
	path=os.path.join(path, title)
	try:
		os.mkdir(path)
	finally:
		return path