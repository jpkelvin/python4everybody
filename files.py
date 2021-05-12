# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open("files/"+fname,"r")
words=fh.read().rstrip()
print(words.upper())
