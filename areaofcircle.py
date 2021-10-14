fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

count = 0

for i in fh:
    if not i.startswith('From '):
        continue
    count = count+1
    aftersplit = i.split()[1]
    print(aftersplit)
        

print("There were", count, "lines in the file with From as the first word")
