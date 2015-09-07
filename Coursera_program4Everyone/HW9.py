"""
Chapter 9 dictionary, hash
"""


import os
os.chdir('C:\Users\Fang\Desktop\Coursera_python')

purse = dict()
purse['Money']=12
purse['Candy']=3
purse['tissues']=75

purse['Candy']=purse['Candy']+2
print purse

## List maintain order, dictionary does not maintain order

ooo={}

ccc=dict()

print 'csev' in ccc


counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print counts

print counts.get(name,0) ## key name, default value if key does not exist



counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print counts


counts = dict()
print 'Enter a line of text:'
line = raw_input('')
words = line.split()
print 'Words:', words

print 'Counting...'
for word in words:
    counts[word]=counts.get(word,0)+1
print 'Counts',counts



counts = {'chuck':1, 'fred':42, 'jan':100}
print list(counts)
print counts.keys()
print counts.values()
print counts.items()


counts = {'chuck':1, 'fred':42, 'jan':100}
for aaa,bbb in counts.items():
    print aaa,bbb



name = raw_input('Enter file:')
handle = open(name,'r')
text = handle.read()
print len(text),text[:40]
words = text.split()

counts=dict()
for word in words:
    if word in counts:       
        counts[word]=counts[word]+1
        print "Word up!", word, counts[word]
    else:
        print "New word", word
        counts[word]=1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount



name = raw_input('Enter file:')
handle = open(name,'r')
text = handle.read()
print len(text),text[:40]
words = text.split()

counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount


#clown file
# the clown ran afer the car and the car ran into the tent and the tent fell down on the clown and the car


