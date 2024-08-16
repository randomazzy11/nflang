#/usr/bin/env python

# - nflang
#terrible coding ahead
import sys
import math
import ast
import shlex
if len(sys.argv) == 1:
    code = ast.literal_eval(shlex.quote(input("Enter code:"))) #copied and pasted from stackoverflow
else:
    code = ast.literal_eval(shlex.quote(open(sys.argv[1], "r").read())) #this looks wrong



if code[len(code)-1] != '':
    print("Last character in the code isnt a  and i decided to make that an error because why not")
    exit()

code = code.split('')

if code[len(code)-1] == '': code.pop() #i dont know why but this thing looks wrong


if code[len(code)-1] != '󰩈':
    print("Last command in the code isnt 󰩈 and i decided to make that an error because why not")
    exit()

for i in range(len(code)):
    code[i] = code[i].split('')


labels = []

for i in range(len(code)):
    if code[i][0] == '󰌕':
        labels.append([code[i][1], i])



cells = [0 for i in range(1024)]

subroutinestack = []
stack = []
idk1 = 0
idk2 = 0
finallyEnded = 0
pointer = 0
cellpointer = 0
compare = False


def getlabel(labelname):
    for i in range(len(labels)):
        if labels[i][0] == labelname:
            return labels[i][1]
    print("Label", labelname, "doesnt exist")
    return -1


while finallyEnded == 0:
    match code[pointer][0]:
        case "":
            stack.append(code[pointer][1])
        case "":
            stack.pop()
        case "":
            stack.append(stack.pop(len(stack)-2))
        case "":
            idk1 = stack.pop()
            sys.stdout.write(str(idk1))
            #this brings the popped thing back idk why and its coded in a weird way
            stack.append(idk1)
        case "󰔊":
            stack.append(input())
        case "":
            stack.append(float(stack.pop()))
        case "":
            stack.append(int(stack.pop()))
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk1 + idk2)
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk1 - idk2)
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk1 * idk2)    
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk1 / idk2) 
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk1 % idk2)
        case "󰩈":
            finallyEnded = 1
        case "󰌕":
            pass
        case "󰌕󰊕":
            subroutinestack.append(pointer)
            pointer = getlabel(code[pointer][1])
        case "󰌕":
            
            pointer = getlabel(code[pointer][1])
        case "󰊕":
            pointer = subroutinestack.pop()
        case "":
            if len(stack) != 0:
                compare = True
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk2)
            stack.append(idk1)
            compare = (idk1 > idk2)
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk2)
            stack.append(idk1)
            compare = (idk1 == idk2)
        case "":
            idk1 = stack.pop()
            idk2 = stack.pop()
            stack.append(idk2)
            stack.append(idk1)
            compare = (idk1 < idk2)
        case "󰊕":
            if compare:
                subroutinestack.append(pointer)
                pointer = getlabel(code[pointer][1])
        case "󰊕":
            if not compare:
                subroutinestack.append(pointer)
                pointer = getlabel(code[pointer][1])
        case "":
            if compare:
                pointer = getlabel(code[pointer][1])   
        case "":
            if not compare:
                pointer = getlabel(code[pointer][1]) 
        case "󰫮":
            stack.append(ord(stack.pop()))
        case "󰫮":
            stack.append(chr(stack.pop()))
        case "󰫮":
            idk1 = list(stack[len(stack)-1])
            
            stack.append(idk1.pop(0))
            stack[len(stack)-2] = ''.join(idk1)
        case "":
            cellpointer = int(stack.pop())%1024
        case "󰍉":
            stack.append(cells[cellpointer])
        case "":
            cells[cellpointer] = int(stack.pop())%256
        case _:
            print("(command", str(pointer)+") idk whats", code[pointer][0], ":(")
            finallyEnded = 1

    pointer += 1


print('\n')

print("Program Finished")
print("Stack:", stack)

