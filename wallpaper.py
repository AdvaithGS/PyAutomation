from time import sleep
from requests import get
from json import loads
import ctypes

wallpaper = loads(get('https://peapix.com/bing/feed?country=in').text)[0]
wallpaper['fullUrl']
with open('wallpaper.jpg','wb') as f:
  content = get(wallpaper['fullUrl']).content
  f.write(content)
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\K Padmavathy\\Downloads\\code\\Automation\\wallpaper.jpg" , 0)
with open('wallpaper.txt','w') as f:
    try:
        f.write(wallpaper['title'])
    except:
        f.write('Unable to map')