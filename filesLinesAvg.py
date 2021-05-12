# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open("files/"+fname)
s=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(":")
    num=float(line[pos+2:])
    s=s+num
    count+=1
print("Average spam confidence:",s/count)
