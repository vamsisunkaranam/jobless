
dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}


while True:
    user_value = input("Enter a number between 1-8 to get associated letter. \n")
    
    if user_value == "thu":
        break
    elif int(user_value) in dict.keys():
        print(dict[int(user_value)])
    else:
        print("Enter Valid Input")
        



