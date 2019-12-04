import csv

instruction_file = open("instructions_altered", 'r')
reader = csv.reader(instruction_file, delimiter=',')

opcodes = reader.__next__()

o=0
while o < len(opcodes):
    opcodes[o] = int(opcodes[o])
    o+=1

o=0
while o < len(opcodes):

    print(opcodes, "\n\n\n")

    if opcodes[o] == 1:
        try:
            operand1_pos = opcodes[o+1]
            operand2_pos = opcodes[o+2]
            operand3_pos = opcodes[o+3]

            result = opcodes[operand1_pos] + opcodes[operand2_pos]
            opcodes[operand3_pos] = result

            o+=3
        except IndexError as e:
            print(e)
            break
    elif opcodes[o] == 2:
        try:
            operand1_pos = opcodes[o+1]
            operand2_pos = opcodes[o+2]
            operand3_pos = opcodes[o+3]

            result = opcodes[operand1_pos] * opcodes[operand2_pos]
            opcodes[operand3_pos] = result

            o+=3
        except IndexError as e:
            print(e)
            break

    o+=1
