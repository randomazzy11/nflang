#  (nflang)
, or nflang (**n**erd **f**ont **lang**uage) is an esolang i made out of boredom, designed to use [nerd font](https://www.nerdfonts.com/) symbols (good luck using it without a [nf font installed](https://www.nerdfonts.com/font-downloads) xD) and in some cases to be unreadable (it just looks like a mess of random characters if you try hard enough). This readme is kinda bad at explaining  and will be replaced by a better esolang wiki page. (not done yet)
## The interpreter
i wanted to write this in javascript so i can put this in a webpage with no need to install anything but i do not know javascript and i barely know python so the code sucks, to install you just clone the github repo and run the main.py file
## Commands/functions and sample programs
this is a really bad command list and will be replaced by a better one when i make the esolang wiki page 
this is a stack-based language with optional brainfuck-like cell memory limited to 1024 cells (which can only go from 0 to 255)

### Commands
if you cant see the characters, or some of the characters look like box drawing go to https://randomazzy11.github.io/nflang
|command|description
|--|--|
||push
||pop
||swap 2 top values on the stack
||print without popping
|󰔊|input
||converts to number (float)
||converts to int
| | adds
| | subtracts
|| multiplies
| | divides
| | modulo
|󰌕 | label
|󰌕 | go to
|󰌕󰊕 | go sub
|󰊕| go sub (compare true)
|󰊕 |  go sub (compare false)
| |  go to (compare true)
| |  go to (compare false)
| |  compare (greater than)
| |  compare (equal)
| |  compare (less than)
| |  compare (is there anything in the stack, sets compare to true if there is)
|󰊕 |  return from sub
|󰫮 |  pop the top thing on the stack and push the unicode number of it
|󰫮| convert a unicode/ascii number from the top of the stack to a character
|󰫮 | delete the first character from the thing at the top of the stack and push it
| |  pops the top of the stack and changes the cell pointer to the popped value
|󰍉 | pushes the value from the currently pointed cell (without ereasing that cell)
| |  pops the top of the stack and changes the value of the currentely pointed cell
|󰩈 -| exits
### Programs/examples
#### Hello World
    Hello, World!\n󰩈
#### [Truth machine](https://esolangs.org/wiki/Truth-machine)
    󰔊1loop󰩈󰌕looploop󰩈
#### Cat program
    󰌕loop󰔊\n󰌕loop󰩈

