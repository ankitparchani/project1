fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()

    start = line.find(':')

    score = float(line[start:].lstrip(": "))

    

    count=count+1
    total = total + score
print("Average spam confidence:", total/count)
