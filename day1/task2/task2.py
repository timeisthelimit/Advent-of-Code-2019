import math

file = open('task1input','r')
modules = file.readlines()

total = 0

for m in modules:
    m = (math.floor(float(m)/3)-2)
    while m > 0 :
        total+=m
        m = (math.floor(float(m)/3)-2)

print(total)