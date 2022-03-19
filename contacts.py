from csv import reader
from sqlite3 import connect
from pyperclip import copy
from time import sleep
conn = connect('db.sql')
c = conn.cursor()
c.execute('select * from contacts')
contacts = list(c.fetchall())

def fn(k):
  return len(k[0])
l= []
with open(input('Enter file name: '), 'r') as f:
  x = list(reader(f))
  print(f'Found {len(x)} contacts')
  sleep(1.15)
  for i in range(len(x[1:])-1):
    if  x[1:][i+1][0] == '' or x[1:][i+1][0] == ' ':
      continue
    name = x[1:][i][0].lower().replace(' ','').replace("\'",'')
    number = x[1:][i][-3].replace(' ','')
    if len(number) > 13:
      number = number[:number.find(':')]
    
    if number.startswith('0'):
        number = "+91" + number[1:]
    
    print(f' {name} - {number}')
    if not number.startswith('+'):
      copy(number)
      change = input('There seems to be something wrong with this number. You can change it or leave it if you think it is right (number copied to clipboard): ')
      number = change if change else number
      print(f'The number is now {number}')
    l.append([name,number])
print()
sleep(1.15)
print('Here are the changed numbers:')
for i,j in l:
  print(i,j)
  if (i,j) not in contacts:
    print('Saving new contact to db')
    with conn:
      c.execute(f'insert into contacts(name,number) values ("{i}","{j}")')