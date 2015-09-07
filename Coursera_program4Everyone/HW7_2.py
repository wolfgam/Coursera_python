fname = raw_input("Enter file name: ")
fh = open(fname)
sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(' ')
    num=float(line[pos:])
    count=count+1
    sum=sum+num   
print 'Average spam confidence:',sum/count
