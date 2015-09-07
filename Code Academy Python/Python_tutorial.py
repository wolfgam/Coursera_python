#http://www.sthurlow.com/python/lesson03/

#A simple program.

'''
print "Mary had a little lamb,"
print "it's fleece was white as snow;"
print "and everywhere that Mary went",
print "her lamb was sure to go."
'''

#variables demonstrated

'''
print "This program is a demo of variables"
v = 1
print "The value of v is now", v
v = v + 1
print "v now equals itself plus one, making it worth", v
v = 51
print "v can store any numerical value, to be used elsewhere."
print "for example, in a sentence. v is now worth", v
print "v times 5 equals", v*5
print "but v still only remains", v
print "to make v five times bigger, you would have to type v = v * 5"
v = v * 5
print "there you go, now v equals", v, "and not", v / 5
'''

#giving variables text, and adding text.
'''
word1 = "Good"
word2 = "Morning"
word3 = "to you too!"
print word1, word2
sentence = word1 + " " + word2 + " " +word3 #put space between words
print sentence
'''

#the while loop

'''
a = 0
while a < 10:
    a = a + 1
print a #if no indent, not in loop, otherwise in loop and will print out 10 numbers
'''

#EXAMPLE
#Type this in, see what it does
'''
x = 10
while x != 0:
    print x
    x = x - 1
    print "wow, we've counted x down, and now it equals", x
print "And now the loop has ended."
'''


#EXAMPLE 1
'''
y = 1
if y == 1:
    print "y still equals 1, I was just checking"
'''

#EXAMPLE 2
'''
print "We will show the odd numbers up to 20"
n=1
while n<=20:
    if n%2==1:
        print n
    n=n+1
print "all done"
'''
'''
a = 10
while a > 0:
    print a
    if a > 5:
        print "Big number!"
    elif a % 2 != 0:
        print "This is an odd number"
        print "It isn't greater than five, either"
    else:
        print "this number isn't greater than 5"
        print "nor is it odd"
        print "feeling special?"
    a = a - 1
    print "we just made 'a' one less than what it was!"
    print "and unless a is not greater than 0, we'll do the loop again."
print "well, it seems as if 'a' is now no bigger than 0!"
print "the loop is now over, and without furthur adue, so is this program!"
'''

# this line makes 'a' equal to whatever you type in
'''
a = raw_input("Type in something, and it will be repeated on screen:")
# this line prints what 'a' is now worth
print a
'''



#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

'''
loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    print "Welcome to calculator.py"

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit calculator.py"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        add1 = input("Add this: ")
        add2 = input("to this: ")
        print add1, "+", add2, "=", add1 + add2
    elif choice == 2:
        sub2 = input("Subtract this: ")
        sub1 = input("from this: ")
        print sub1, "-", sub2, "=", sub1 - sub2
    elif choice == 3:
        mul1 = input("Multiply this: ")
        mul2 = input("with this: ")
        print mul1, "*", mul2, "=", mul1 * mul2
    elif choice == 4:
        div1 = input("Divide this: ")
        div2 = input("by this: ")
        print div1, "/", div2, "=", div1 / div2
    elif choice == 5:
        loop = 0
	
print "Thankyou for using calculator.py!"


def funnyfunction(first_word,second_word,third_word):
    print "The word created is: " + first_word + second_word + third_word
    return first_word + second_word + third_word
'''

# calculator program

'''
# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice
def menu():
    #print what options you have
    print "Welcome to calculator.py"
    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit calculator.py"
    print " "
    return input ("Choose your option: ")
    
# this adds two numbers given
def add(a,b):
    print a, "+", b, "=", a + b
    
# this subtracts two numbers given
def sub(a,b):
    print b, "-", a, "=", b - a
    
# this multiplies two numbers given
def mul(a,b):
    print a, "*", b, "=", a * b
    
# this divides two numbers given
def div(a,b):
    print a, "/", b, "=", a / b
    
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "),input("to this: "))

    elif choice == 2:
        sub(input("Subtract this: "),input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop = 0

print "Thankyou for using calculator.py!"

# NOW THE PROGRAM REALLY FINISHES


months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')
'''

#A few examples of a dictionary

#First we define the dictionary
#it will have nothing in it this time
ages = {}

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if ages.has_key('Sue'):
    print "Sue is in the dictionary. She is", \
ages['Sue'], "years old"

else:
    print "Sue is not in the dictionary"

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print "The following people are in the dictionary:"
print ages.keys()

#You could use this function to
#put all the key names in a list:
keys = ages.keys()

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print "People are aged the following:", \
ages.values()

#Put it in a list:
values = ages.values()

#You can sort lists, with the sort() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print keys
keys.sort()
print keys

print values
values.sort()
print values

#You can find the number of entries
#with the len() function:
print "The dictionary has", \
len(ages), "entries in it"

