handle = open('mbox.txt','r') ## r for read, w for write
## It's not going to read the file, just create connection between memory and hard drive, since memory is small

stuff='Hello\nWorld'
print stuff

stuff = 'X\nY'
len(stuff)  #3

fhand=open('mbox-short.txt')
count=0
for line in fhand:
    line=line.rstrip()
    # Skip uninteresting lines
    if not line.startswith('From:'):
        continue
   
    #if line.startswith('From:'):
        count=count+1
        print line


fhand=open('mbox-short.txt')
count=0
for line in fhand:
    line=line.rstrip()
    # Skip uninteresting lines
    if not '@uct.ac.za' in line:
        continue
        print line

fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print 'There were' , count, 'Subject lines in', fname

import os
os.chdir('C:\Users\Fang\Desktop\Coursera_python')

fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = 'words.txt'
fhan = open(fname)
for line in fh:
    line=line.rstrip()  
    print line.upper()
