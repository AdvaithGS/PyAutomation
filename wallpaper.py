import asyncio
from time import sleep
from requests import get
from json import loads
import ctypes

async def set_wallpaper():
  print('This')
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
  sleep(3600)
loop = asyncio.new_event_loop()
loop.run_forever()