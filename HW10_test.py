### Chapter 10 Tuples


'''
## list is mutable
x = [9.8,7]
x[2] = 6
print x ## 9,8,6


## Tuples are immutable

z = (5,4,3)
z[2]=0
## trackback error

##You cannot sort/append/reverse  x.reverse()
t=tuple()
dir(t)  # count index

## Python does not need to build tuple structures to be modifiable,
tuples are simpler and more efficient in memory use and performance than lists

## if we make temporary variables, we prefer tuples over lists

(a,b)=(99,98) so a is assigned 99, b is assigned 98, tuples

a,b=(99,98) a=99, b=98, both tuples
## The items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] =2
d['cwen'] = 4

for (k,v) in d.items():
    print k,v

tups = d.items()

print tupds ## list of tuples

## tuples are comparable, if first item equal, go to next. only look at the items that differ. and ignore the next items

## sort by keys
d = {'a':10,'b':1,'c':22}
t=d.items() ## t is a list of tuples
t.sort() 
t = sorted(d.items())

for k,v in sorted(d.items()):
    print k,v

## sort by values instead of keys

c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

print tmp
tmp.sort(reverse=True)
    
'''
'''
import os
os.chdir('C:\Users\Fang\Desktop\Coursera_python')

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst = list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)
lst.sort(reverse=True)
for val,key in lst[:10]:
    print key,val


c = {'a':10,'b':1,'c':22}
print sorted([(v,k) for k,v in c.items()])

##within [] is list comprehension

'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From:'):continue
    if line.startswith('From'):
        words=line.split()
        hrs = words[5]
        hr = hrs.split(':')
        hr0=hr[0]
        counts[hr0]=counts.get(hr0,0)+1

t=counts.items()
t.sort()
lst = list()
for hr,cnt in counts.items():
    newtup = (cnt,hr)
    lst.append(newtup)
lst.sort(reverse=True)
for cnt,hr in lst:
    print hr,cnt

'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From:'):continue
    if line.startswith('From'):
        words=line.split()
        hrs = words[5][:2]
        counts[hrs]=counts.get(hrs,0)+1

t=counts.items()
t.sort()
print t    
'''    

