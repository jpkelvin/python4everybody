import re
num=list()
handle= open('files/regex_sum_1215511.txt')
for line in handle:
    line.rstrip()
    a = re.findall('[0-9]+',line)
    if len(a) < 1:continue
    for i in a:
        num.append(int(i))
print(sum(num))
