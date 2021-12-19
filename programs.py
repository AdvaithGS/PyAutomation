from sqlitedict import SqliteDict
from os import popen
from webbrowser import open_new_tab
db = SqliteDict('./db.sqlite',autocommit = True)
while True:
    prog = input('Enter command: ')
    try:
        if db[prog][0] == 1:
            popen(db[prog][1])            
        else:
            open_new_tab(db[prog][1])
        print(f'Opening {prog} at {db[prog][1]}')
    except:
        if prog.startswith('add'):
            lst = list(prog.split(' ',3))
            if name not in db.keys():
                name,num,loc = lst[1],int(lst[2]),lst[3]
                db[name] = [num,loc]
            else:
                print('Name already in list') 
        elif prog.startswith('exit'):
            exit()  
        else:
            print('Not available in database')
