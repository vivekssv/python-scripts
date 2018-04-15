#!/usr/bin/python
#############################################################################################
#Maintance - Array of index, forloop and if and else condition covered.                     #
#############################################################################################
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
for brands in computer_brands:
    if brands == 'Asus':
        print ("" + brands + "Tek Computer Inc. is a Taiwanese multinational computer") 
    elif brands == 'Apple':
        print ("" + brands + " is an American multinational technology company headquartered in Cupertino")
    elif brands == 'Dell':
        print ("" + brands + " is an American multinational computer technology company based in Round Rock")
    else:
        print ( "" + brands + " is a South Korean multinational conglomerate...")