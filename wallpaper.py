from requests import get
from bs4 import BeautifulSoup
import ctypes
req = get('https://peapix.com/bing').text
soup = BeautifulSoup(req,'lxml')
url = soup.find('div',attrs = {'class': 'image-list__picture lazyload'}).get('data-bgset')
url = url[:-7] + '1080.jpg'
with open('wallpaper.jpg','wb') as f:
  content = get(url).content
  f.write(content)
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\K Padmavathy\\Downloads\\code\\Automation\\wallpaper.jpg" , 0)