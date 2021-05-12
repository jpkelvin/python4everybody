name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open('files/'+name)
hrs=list()
count=dict()
for line in handle:
    if line.startswith("From "):
        line.rstrip()
        words= line.split()
        time=words[5].split(":")
        hrs.append(time[0])
for hour in hrs:
    count[hour]=count.get(hour,0)+1
tmp=sorted([(k,v) for k,v in count.items()])
for k,v in tmp:
    print(k,v)
