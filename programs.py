from sqlitedict import SqliteDict
from os import popen
from webbrowser import open_new_tab
db = SqliteDict('./db.sqlite',autocommit = True)
while True:
    prog = input('Enter command: ')
    try:
        if db[prog][0] == 'app':
            popen(db[prog][1])            
        else:
            open_new_tab(db[prog][1])
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
            exit() 
        elif prog.startswith('remove'):
            com,name = prog.split()
            if input(f'Are you sure you want to remove {db[name]}? : ').lower() == 'y':
                 del db[name]
                 print('Deleted.')
        elif prog.startswith('list'):
            i = 1
            for key in db.keys():
                print(f'   {i}. {key} - {db[key][1]}',end = '\n')
                i += 1
        else:
            print('Not available in database')
