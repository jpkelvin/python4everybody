fname = input("Enter file name: ")
fh = open('files/'+fname)
lst = list()
for line in fh:
    line.rstrip()
    a=line.split()
    for i in a:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
