from sqlitedict import SqliteDict
from os import popen
from requests import get
from bs4 import BeautifulSoup
from webbrowser import open_new_tab
from pyautogui import hotkey
import pyautogui as pgui
from time import sleep
import sqlite3
conn = sqlite3.connect('db.sql')
c = conn.cursor()
db = SqliteDict('./db.sqlite', autocommit = True)
while True:
    prog = input('Enter command >> ')
    try:
        if db[prog][0] == 'app':
            popen(db[prog][1])            
        elif db[prog][0] == 'url':
            open_new_tab(db[prog][1])
        elif db[prog][0] == 'hotkey':
            try:
                hotkey(db[prog][1].split('+')[0],db[prog][1].split('+')[1],db[prog][1].split('+')[2])
            except:
                hotkey(db[prog][1].split('+')[0],db[prog][1].split('+')[1])
        print(f'Opening {prog} at {db[prog][1]}')
    except:
        if prog.startswith('add'):
            lst = list(prog.split(' ',3))
            type,name,loc = lst[1],lst[2],lst[3]
            if name not in db.keys():
                db[name] = [type,loc]
                print(f'Added {name} at {loc} to database')
            else:
                print('Name already in list') 
        elif prog.startswith('exit'):
            quit() 
        elif prog.startswith('define'):
            req = get(f'http://wordnetweb.princeton.edu/perl/webwn?s={prog.split()[1]}').text
            soup = BeautifulSoup(req,'lxml')
            try:
                print(soup.find('li').text)
            except:
                print('Cant find definition.')
        elif prog.startswith('note'):
            if prog.split()[1] == 'add':
                db['note'] += [prog.split(' ',2)[2]]
                print('Added note.')
            elif prog.split()[1] == 'list':
                x = 1
                for i in db['note']:
                    print(f'{x}. {i}')
                    x += 1
            elif prog.split()[1] == 'remove':
                print(db['note'][int(prog.split(' ',2)[2]) - 1])
                db['note'] = db['note'][:int(prog.split(' ',2)[2]) - 1] + db['note'][int(prog.split(' ',2)[2]):]
                print('Removed.')
        elif prog.startswith('remove'):
            com,name = prog.split()
            if input(f'Are you sure you want to remove {name} at {db[name][1]}? : ').lower() == 'y':
                 del db[name]
                 print('Deleted.')
        elif prog.startswith('schema'):
            print('Add <type - app/url> <name> <url/location> ')
        elif prog.startswith('list'):
            i = 1
            for key in list(db.keys()):
                if key != 'note':
                    print(f'   {i}. {key} - {db[key][1]}',end = '\n')
                    i += 1
        elif prog.startswith('whatsapp'):
            lst = prog.split(' ',2)
            name = lst[1]
            mes = lst[2].replace(' ','%20')
            c.execute(f'select * from contacts where name = "{name}"')
            lst = c.fetchall()[0]
            print('It shall be done.')
            open_new_tab(f'https://web.whatsapp.com/send?phone={lst[1]}&text={mes}')
            sleep(80)
            width,height = pgui.size()
            pgui.click(width/2,height/2)
            pgui.press('enter')
        else:
            print('Not available in database')
