data_list = list((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,34,76,23,44,322,323))

check_data = int(input("check availability:"))

min = 0
max = 0
list_reset = data_list
middle_value = 0
middle = None 

while True:
   

    if int(len(list_reset)) %2 == 0:
        print("got here")
        middle = int(len(list_reset)/2)
        middle_value = list_reset[middle]
        print(middle_value)

    else: 
        middle = int((len(list_reset)-1)/2)
        print(middle)   
        middle_value = list_reset[middle]
    print("check data" + str(check_data), str(middle_value))

    if check_data > middle_value:
        list_reset = list_reset[middle:]    
        # print(list_reset)

    elif check_data < middle_value:
        list_reset = list_reset[:middle]
        print(list_reset)


    elif check_data == middle_value:
        list_reset = data_list
        print("found")
        break

    if len(list_reset)==1:
        if list_reset[0] == check_data:
            list_reset = data_list
            print("found")
            break

        else:
            list_reset = data_list
            print("not found")
            break
    



# print(data_list[middle])

# print(middle)




