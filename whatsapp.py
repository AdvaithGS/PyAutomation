from webbrowser import open_new_tab
import pyautogui as pgui
from sqlite3 import connect
from time import sleep
from os import system
conn = connect('db.sql')
c = conn.cursor()

def get_contact(name:str):
  c.execute(f'select * from contacts where name = "{name}"')
  lst = c.fetchall()
  try:
    return lst[0][1]
  except:
     return False

def send_message(name:str,mes:str,when:int,shutdown:bool = False,close:bool = False):
  mes = mes.replace(' ','%20')
  if not get_contact(name):
    return False
  num = get_contact(name)
  type_num = 'phone=' if num.startswith('+') else 'code='
  text = '&text=' + mes if num.startswith('+') else ''
  sleep(when)
  open_new_tab(f'https://web.whatsapp.com/send?{type_num}{num}{text}')
  sleep(80)
  pgui.hotkey('win','up')
  sleep(3)
  width,height = pgui.size()
  pgui.click(width/2,height - 75)
  if type_num == 'code=':
    pgui.write(mes)
  pgui.press('enter')
  if close:
    sleep(2)
    pgui.hotkey('ctrl','w')
  if shutdown:
    system('shutdown /sg')
  return True
