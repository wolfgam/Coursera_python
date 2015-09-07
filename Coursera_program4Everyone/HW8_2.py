"""
fh=open('romeo.txt')
lst = list()
for line in fh:
    line=line.rstrip()
    if line == '':continue
    print '----',line
    words=line.split()
    print '++++',words
    if len(words)==0:continue
    ###print words
    for word in words:
        print '==',word
        if word not in lst:
            lst.append(word)
lst.sort()    
print lst
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if line == '':continue
    if line.startswith('From:'):continue
    if line.startswith('From'):
        words=line.split()
        count=count+1
        print words[1]     

print "There were", count, "lines in the file with From as the first word"
