from webbrowser import open_new_tab
from os import popen
from pyautogui import hotkey
choice= int(input('Enter choice: '))
if choice == 1:
    open_new_tab('https://discord.com/app')
    open_new_tab('https://mail.google.com')
    x = popen('C:\\Users\\K Padmavathy\\AppData\\Local\\Microsoft\\Teams\\update.exe')
    open_new_tab('https://top.gg/bot/792458754208956466/vote')
    open_new_tab('https://discordbotlist.com/bots/astrobot-2515/upvote')
elif choice == 2:
    hotkey('Win','5')#opens whatsapp on my pc
    open_new_tab('https://discord.com/app')
    open_new_tab('https://mail.google.com')
    x = popen('C:\\Users\\K Padmavathy\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    open_new_tab('https://top.gg/bot/792458754208956466/vote')
    open_new_tab('https://discordbotlist.com/bots/astrobot-2515/upvote')
elif choice == 3:
    x = popen('C:\Windows\explorer.exe')
    open_new_tab('https://discord.com/app')
    open_new_tab('https://mail.google.com')
    open_new_tab('https://top.gg/bot/792458754208956466/vote')
    open_new_tab('https://discordbotlist.com/bots/astrobot-2515/upvote')
import programs
