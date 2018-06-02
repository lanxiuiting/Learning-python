#write.py
def make_story1():
  f= open('story.txt','w')
  f.write('Mary had a little lamb,\n')
  f.write('and then she had some more.\n')
import os
def make_story2(): 
  if os.path.isfile('story.txt'):
    print('story.txt already exists')
  else:
    f= open('story.txt','w')
    f.write('Mary had a little lamb,\n')
    f.write('and then she had some more.\n')
def add_to_story():
  f=open('story.txt','a')
  f.write('Mary and mike go to zoo.\n')
def insert_title():
  f =open('story.txt','r+')
  temp= f.read()
  temp='Mary story'+'\n\n'+temp
  f.seek(0)
  f.write(temp)
