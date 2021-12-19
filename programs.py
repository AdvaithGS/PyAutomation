from sqlitedict import SqliteDict
from os import popen
from webbrowser import open_new_tab
db = SqliteDict('./db.sqlite',autocommit = True)
while True:
    prog = input('Enter program/app to load: ')
    try:
        if db[prog][0] == 1:
            popen(db[prog][1])            
        else:
            open_new_tab(db[prog][1])
        print(f'Opening {prog} at {db[prog][1]}')
    except:
        if prog.startswith('add'):
            
        print('Not available')
