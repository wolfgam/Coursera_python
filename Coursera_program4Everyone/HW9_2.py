name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand=open('mbox-short.txt')
count=dict()
manyemail=None
manyemailcnt=None

for line in fhand:
    line=line.rstrip()
    # Skip uninteresting lines
    if not line.startswith('From:'):
        continue
    words=line.split()
    email = words[1]
    count[email]=count.get(email,0)+1
        
for email,cnt in count.items():
    if manyemailcnt is None or manyemailcnt<cnt:
        manyemail = email
        manyemailcnt = cnt
print manyemail,manyemailcnt


