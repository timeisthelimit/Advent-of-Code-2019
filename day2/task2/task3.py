def runop(memory, i, j, o=0):
    memory[1] = i
    memory[2] = j
    while o < len(memory):

        if memory[o] == 99:
            return memory[0]

        if memory[o] == 1:
            try:
                operand1_pos = memory[o+1]
                operand2_pos = memory[o+2]
                operand3_pos = memory[o+3]

                result = memory[operand1_pos] + memory[operand2_pos]
                memory[operand3_pos] = result

                o+=3
            except IndexError as e:
                print(e)
                break
        elif memory[o] == 2:
            try:
                operand1_pos = memory[o+1]
                operand2_pos = memory[o+2]
                operand3_pos = memory[o+3]

                result = memory[operand1_pos] * memory[operand2_pos]
                memory[operand3_pos] = result

                o+=3
            except IndexError as e:
                print(e)
                break
        o+=1

import csv
import sys

instruction_file = open("instructions_altered", 'r')
reader = csv.reader(instruction_file, delimiter=',')

opcodes = reader.__next__()

o=0
while o < len(opcodes):
    opcodes[o] = int(opcodes[o])
    o+=1


for i in range(0,100):
    for j in range(0,100):
        if runop(opcodes[:], i, j) == 19690720:
            print(i, j) 