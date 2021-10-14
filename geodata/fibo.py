febo_range = int(input("please enter febo range:"))

a, b = 0, 1
count = 0


while count < febo_range:
    print(a)
    c= a+b
    a = b
    b = c
    count+=1

