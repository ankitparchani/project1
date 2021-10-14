count = dict()


name = input("Enter file:")
handle = open(name)

if len(name) < 1: name = "mbox-short.txt"
for i in handle:
    if not i.startswith('From '):
        continue
    afterslice = i.split()[5]
    line=afterslice[0:2]
    count[line] = count.get(line,0)+1
        
lst=list()        
for (value,count) in sorted(count.items()):
    lst.append((value,count))
    print(value, count)

# lst.sort()
# for value,count in lst:
#     print (value,count)

