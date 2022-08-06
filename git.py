import os
import sys
sys.stdout = open(os.devnull,'w')
os.chdir('..')
for dir in os.listdir():
  if os.path.isdir(os.path.join(os.path.abspath('.'),dir)):
    os.chdir(dir)
    x = os.system('git pull')
    os.chdir('..')
os.chdir('Automation')
sys.stdout = sys.__stdout__