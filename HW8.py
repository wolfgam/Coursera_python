## lists, collection


fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    words=line.split()
    if words[0]!='From':continue
    print words[2]


friends = ['Joseph','Glenn','Sally']
friends.sort()
for i in range(len(friends)):
    friend=friends[i]
    print 'Happy New Year:',friend


friend in friends:
    print 'Happy New Year:',friend


stuff=list()
stuff.append('book')
stuff.append(99)
stuff.append9('cookie')
99 in stuff # true

numlist = list()
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print 'Average:', average

count=0
total=0
while True:
    inp=raw_input('Enter a number:')
    if inp == 'done':break
    value = float(inp)
    total = total+value
    count = count+1
average = total/count
print 'Average:',average


abc='With three words'
stuff = abc.split()
print stuff

for w in stuff:
    print w

line = 'A lot                of space'
line.split() # omit space
line = 'first;second;third'
thing = line.split(';')

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
print words[2]

words=line.split()
email=words[1]
pieces=email.split('@')
print pieces[1]

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line == '':continue
    words=line.split()
    #if words ==[]:continue  ## or if len(words)<1:continue  
    if words[0]!='From':continue
    print '============',words[2] ## debug use
