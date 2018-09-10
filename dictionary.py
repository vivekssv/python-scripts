#!/usr/bin/python
import sys

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