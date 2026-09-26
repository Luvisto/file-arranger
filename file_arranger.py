#This is a file arranger for you
import os
import shutil as s
import time

folder="."
tf='Texts'
py='pythons'
if not os.path.exists(tf):
    os.mkdir(tf)
else:
    print('The file exists')
print(f'Moving unmoved files {tf}..........')
time.sleep(5)
for file in os.listdir(folder):
    if os.path.isfile(file):
      #  print(file)
        if file.endswith('.txt'):
            print(file)
            s.move(file,os.path.join(tf,file))


if not os.path.exists(py):
    os.mkdir(py) 
print(f'Moving unmoved files {py}..........')
for file1 in os.listdir(folder):
    if os.path.isfile(file1):
        if file1.endswith('.py'):
            print(file1)
#            except:
#            if file1='browser_opener.py'
            s.move(file1,os.path.join(py,file1))
