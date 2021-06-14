

# ComDown

This is just simple porn/hentai comics downloader. Which simply downloads the image from the comics-webpages. This project support multiple hentai/porn comics websites. So what gives me this project idea? Well, while I tried to read comics on the different comics webpages its difficult to read for advertisement or poor webpage degine or slow bandwitdh and also for some reason you want to download full comic to read offline but you can't because the websites don't provide any functionality to download. So I searched for hentai downloader projects on github but I didn't find any project that support multiple websites at the same time. I've just learned python, and my school is closeed, so why don't I make my own hentai comics downloader. And I made one. Thats the story


## About
 This python project will simply download porn comics or hentai comics. It also support batch / bulk, chapter / episode download. This Hentai comics downloader is easy to use. This porn comic downloader is written in pyhton, so It is supported in multiple OS, even in **Android**



  
## Supported Sites

- allporncomic.com (Chapter Download Supported)
- multporn.net
- nhentai.net
- azporncomic.com

  ## Installation
This project is written in Python 3. So you need to install python3 in our pc or smartphone.

### For Windows, Mac, Linux, Termux
1. Install python 3 (Your can follow Youtube turorial how to install python 3 on your OS)
2. Check if the python 3 and pip is installed successfully:
```bash

    python --version

```
```bash

    pip --version

```
your python version should be avobe **3.0**\
3. Create a virtual environment if you need to.(If you don't know about it ignore this step)\
4. Install python dependencies using following command
```bash 

    pip install -r requirements.txt

```
5. Download or clone the project.
6. Go to your project directory in your terminal or command prompt. in my case:
```bash 

    cd Downloads/ComDown/

```
5. Edit the `option.txt` according to your desire.(option.txt is written in json format)
6. run the `app.py` using the following command: 
```bash 

    python app.py

```
7. Your all done. The project should run properly.

### For Android
1. Download this reporigitroy (make sure you turn your desktop view/Mode in your browsor, as github doesn't allow you to download in mobile view.)
2. Install pyDorid 3 from Play Store and open it
3. Go to pip in menu. In 'Library name' type `requests`, `bs4`, `termcolor` and tap on instal. Wait until installation is complete.
4. Go back and tap on file icon and select open. After find where you downloaded the repository file(1no steps) and open `option.txt`.
5. edit it and save it
6. open the `app.py` same way
7. tap on run icon and it should start the project without any error
* you can also use `Termux` if you know how to use it.
* Don't forget to give the app storage permisson, so it can write data
### For IOS 
you can use `Pythonista 3` which support python 3 with Library. I'm not sure if it work properly cause I don't have iphone
## Usage/Examples

I found that everytime writting command and passing argunment is painful, so I developed the project based on   `option.txt`\
After Editing `option.txt` just run `python app.py` or `python3 app.py` depands on your device.
### Downloading a single comic
open `option.txt` and edit according following example argunment:
```

    "workingMode":"1",
    "link": "https://allporncomic.com/porncomic/sultry-summer-ben-10-incognitymous/3-sultry-summer/",
    "path": "./desktop/data/",
    "thread": "3",

```
save it and simply run the `app.py`. It will start downloading in your desktop data(! don't use this directory, someone can see it, its just an example) folder.
### Downloading with multiple links
1. first create or edit(if exists) links.txt and paste the comics links that you want to download. In my case:
```
    https://allporncomic.com/porncomic/sultry-summer-ben-10-incognitymous/3-sultry-summer/
    https://nhentai.net/g/348548/
    https://multporn.net/comics/the_incredibles/the_incestibles

```
save it.\
2. open `option.txt` and edit according following example argunment:
```

    "workingMode":"2",
    "textPath":"links.txt"
    "path": "./desktop/data/",
    "thread": "3",

```
Save it, run `app.py` and it will download all the comics one by one
### Downloading the whole chapter(ChapterMode)(Only supported websites)
open `option.txt` and edit according following example argunment:
```

    "workingMode":"3",
    "link": "https://allporncomic.com/porncomic/sultry-summer-ben-10-incognitymous/",
    "path": "./desktop/data/",
    "thread": "3",

```
save it and run `python app.py` it will download the whole series from start to end.

* Sorry for doing it unprofessetional way.



  
