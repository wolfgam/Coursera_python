largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    if len(inp)<1 : break
    
    try:
        num=float(inp)
    except:
        print 'Invalid input'
        continue
    largest = max(largest,num)
    smallest = min(smallest,num)

print 'Maximum is',int(largest)
print 'Minimum is',int(smallest)
