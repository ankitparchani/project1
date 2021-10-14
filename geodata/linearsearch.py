data_list = ["ankit", "Arshad", "Atul", "Uday"]

check_data = input("check availability:")


for i in data_list:
    if i==check_data:
        print("position " + str(data_list.index(i)))
        break

else:
    print("Found nothing")

print("Thankyou")

