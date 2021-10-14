fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word= line.strip().split(" =>", 1)[0]
    print(word)
    with open('romeo.txt', 'a') as fh:
        fh.writelines(word)

    for element in word:               
        if element in lst:         
            continue               
        else :                     
            lst.append(element)                                  
# print (lst) 
