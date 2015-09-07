'''
def fred():
   print "Zap"

def jane():
   print "ABC"
fred()
jane()
fred()




lst = [1,2,3]

abc = None
for val in lst:
    if abc == None or val > abc:
        abc = val

print abc


abc = "With three words"
stuff = abc.split()
print len(stuff)



stuff = ['joseph', 'sally', 'walter', 'tim']
print stuff[2]


lst = []
lst.append(4)
lst.append(10)
lst.append(21)
lst.append(6)
print lst[2]


def hello():
    print "Hello" 
    print "There"

x = 10
x = x + 1


sta = "abc"
stb = "123"
stc = sta + stb
print stc



fline = "blah blah"

if len(fline) > 1 :
    print "More than one"
    if fline[0] == "h" : 
        print "Has an h"
print "All done"


def hello():
    print "Hello"
    print "Fun"
 
hello()
hello()


total = 0
count = 0
for abc in [3, 41, 12, 9, 74, 15] : 
    total = total + abc
    count = 1
ave = total / count
print ave


x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value < x :
        x = value 
print x


a = "123"
b = 456
c = a + b

str = "hello there bob"
print str[0]


str = "hello there bob"
print str[4]


stuff = ['joseph', 'sally', 'walter', 'tim']
print stuff[2]

'''
st = "abc"
ix  = int(st)
