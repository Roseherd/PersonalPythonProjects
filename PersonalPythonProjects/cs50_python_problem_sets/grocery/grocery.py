grocery_list = {}
#Continue allowing the user to input items line by line using a loop
while True:
    try:
        #Allow user to input items and Output the grocery list in all uppercase
        items = input().upper()
    #Add each item of grocery list to a dictionary
        if items in grocery_list:
            grocery_list[items] += 1
        else:
            grocery_list[items] = 1
    except EOFError:
        print()
        break
    except KeyError:
        pass
#Sort the list alphabetically
sorted_groceries = sorted(grocery_list.keys())

for grocery in sorted_groceries:
    #Prefix each line with number of times user inputted that item
    print(grocery_list[grocery], grocery)



