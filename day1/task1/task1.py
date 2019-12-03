import math

file = open('task1input','r')
modules = file.readlines()

total = 0

for m in modules:
    total+=(math.floor(int(m)/3)-2)

print(total)