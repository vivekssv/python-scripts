#!/usr/bin/python
#############################################################################################
#Maintance - Array of index, forloop and if and else condition covered.                     #
#############################################################################################
computer_brands = ["Apple", "Asus", "Dell", "Samsung", "redmi"]
computer_rates = ["300$", "100$", "250$", "90$"]
for brands in computer_brands:
    if brands == 'Asus':
        print ("" + brands + "Tek Computer Inc. laptop rates {}".format(computer_rates[1])) 
    elif brands == 'Apple':
        print ("" + brands + " laptop rates {}".format(computer_rates[0]))
    elif brands == 'Dell':
        print ("" + brands + " laptop rates {}".format(computer_rates[2]))
    elif brands == 'Samsung':
        print ( "" + brands + " laptop rates {}".format(computer_rates[3])) 
    else:
        print ("The {} doesn't have laptop versions".format(brands))