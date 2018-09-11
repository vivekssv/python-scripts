#!/usr/bin/python
#[
#{
#"column_a": 1,
#"column_b": 1,
#"column_c": 10
#},
#{
#"column_a": 2,
#"column_b": 4,
#"column_c": 8
#},
#{
#"column_a": 3,
#"column_b": 9,
#"column_c": 6
#},
#{
#"column_a": 4,
#"column_b": 16,
#"column_c": 4
#},
#{
#"column_a": 5,
#"column_b": 25,
#"column_c": 2
#}
#]
import sys
import json
from httplib2 import HTTPConnectionWithTimeout
from urllib.request import urlopen
print ("Please provide the column with value to display the reslut, column_a, column_b EX:")
column_number = input(str())
print (column_number)
github_jsondate = "https://raw.githubusercontent.com/vinothsundararajan/python-scripts/master/jsonheaders/sample_num.json"
jsongit = urlopen(github_jsondate)
jsonoutput = jsongit.read()
gitjson = json.loads(jsonoutput)
try:
    print (gitjson)
    for i in gitjson:
        print ("{} = ".format(column_number), i[column_number])
except TypeError:
    print("Python unable to handle the request")