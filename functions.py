#!/usr/bin/python3
#arug
from sys import argv
s1 = int(argv[1])
s2 = int(argv[2])
# function
def hello(x,y):
    print ("Hello world")
    sum = x + y
    sub = x - y
    mul = x * y
    div = x / y
    mol = x % y
    print (sum,sub,mul,div,mol)
#main program
if s1 is None:
    print ("Missing input params s1")
    exit(0)
elif s2 is None:
    print ("Missing input params s2")
    exit(0)
else:
    hello(s1,s2)