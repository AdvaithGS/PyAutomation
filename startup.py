from time import strftime
from webbrowser import open_new_tab
from os import popen
from pyautogui import hotkey
time = int(strftime('%H'))
popen('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
if time in range(8,10):
    open_new_tab('https://teams.microsoft.com')
elif time in range(9,12):
    hotkey('Win','6')
    popen('C:\\Users\\K Padmavathy\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
else:
    popen('C:\Windows\explorer.exe')
    open_new_tab('https://discord.com/app')
    open_new_tab('https://mail.google.com')
exit()
