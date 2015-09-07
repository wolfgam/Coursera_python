fruit = 'banana'
pos = fruit.find('na')
banana.upper()
banana.lower()
greet = ' Hello Bob '
nstr = greet.replace('Bob','Jane')
print greet.replace('o','X')
greet.lstrip()
greet.rstrip()
greet.strip()
line='Please have a nice day'
line.startswith('Please')

## Parsing the txt
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos=data.find(' ',atpos) ## starting at @ sign, where is the space
data[tops+1:sppos] ## +1 so not including@, and sppos, up to but not including space

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(' ')
txt_num = text[pos:].lstrip()
num = float(txt_num)
print num
float(text[text.find(' '):])
