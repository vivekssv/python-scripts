#!/usr/bin/python
import sys
import json
json_data = """ {
    "text key": "string",
    "integer key": 123,
    "boolean key": true,
    "simple list": [
        "value 1",
        "value 2"
    ],
    "dict": {
        "element 1": "value E.1",
        "element 2": "value E.2"
    },
    "dict list": [
        {
            "key 1.1": "value 1.1",
            "key 1.2": "value 1.2"
        },
        {
            "key 2.1": "value 2.1",
            "key 2.2": "value 2.2"
        }
    ]
} """
my_dictionary = json.loads(json_data)
print(my_dictionary, indent=4)

STUDENTS={
    'VINOTH' : ['90','80','70'],
    'VIVEK' : ['89','79','79'],
    'SEKAR' : ['77','99','88']
}
#print (STUDENTS.keys())
arugument=sys.argv[1]
try:
    if sys.argv[1] == 'VINOTH' or sys.argv[1] == 'VIVEK' or sys.argv[1] == 'SEKAR':
        print("success")
        for key in STUDENTS.keys():
            whatvalue = STUDENTS[key]
            if key == arugument :
                #print (key, "=", whatvalue)
                print ("Filtering my mark's alone from dictionary",key, "=", whatvalue)
                break
            else:
                print ("Unknown user score you can get if u pass the username {}".format(STUDENTS[key]))
except:
    print ("Please atleast pass one user name form the list VINOTH,VIVEK or SEKAR, thanks")
    sys.exit(0)