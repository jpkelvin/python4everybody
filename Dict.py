name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open('files/'+name)
mails=list()
count=dict()
for line in handle:
    if line.startswith('From '):
        line.rstrip()
        a=line.split()
        mails.append(a[1])
for word in mails:
    count[word]=count.get(word,0)+1
bigWord=None
bigCount=None
for k,v in count.items():
    if bigCount is None or v > bigCount:
        bigWord=k
        bigCount=v
print(bigWord,bigCount)
