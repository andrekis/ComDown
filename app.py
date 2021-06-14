#author Imon
#project_name: ComDown
#version: 0.1
#starting_at: 7.27, 15 feb 2021
#development: currently running
from tools.txtsync import sync
from tools.console import *
from tools.modes import *
from tools.jsonedit import *

# workingMode,
# downloaded,
# thread,
# link,
# path,
# txtpath

data=sync()
# clearing app data
obj={}
setdata(obj)
refresh()
# print(type(data))
if int(data['workingMode']) == 1:
    singleMode(data)
elif int(data['workingMode']) == 2:
    multiMode(data)
elif int(data['workingMode']) == 3:
    chapMode(data)
else:
    error('worlingMode error')
