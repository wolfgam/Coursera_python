count=0
total=0
while True:
    inp = raw_input('Enter a number: ')
    # Don't Count here!
    if inp == 'Done': break
    if len(inp)<1 : break #check for empty line#

    # Do the work
    try:
        num = float(inp)
    except:
        print 'invalid input'
        continue
    count=count+1
    total=total+num
    print num,total,count

print 'Average:', total/count
