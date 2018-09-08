# Duko.py is a 3*3 Sudoku solving Python program, enabled by Big Data and AI (Totally not backtracking and recursion)

**The file doku.py was written by F4dora_0f_d00m.
If you want access to make changes to this repository, ask questiosn or 
give any sort of feedback, be free to contact me.**

**This Python file is free for all to use. If you find it useful somehow,
be sure to tell me**


### User's Guide
Currently, only .csv files are supported. Make sure the files are formatted like in the example files.
The program was written with Python3 in mind.

If you just want to print the output:
```
    python3 doku.py [csv file containing the board]
```

If you want to output the solution to a file:
```
    python3 doku.py -i [csv file containing the board] -o [name of the output file]
```
Alternatively, you can:
```
    python3 doku.py --in [csv file containing the board] --out [name of the output file]
```

If you want to output the solution to a file AND print the output, add the -p flag:
```
    python3 doku.py ... -p
```
Alternatively, you can:
```
    python3 doku.py ... --print
```

### A few notes:
    * If a board is impossible, the program goes into an infinite loop. All possible boards
     can be solved in a matter of seconds (depending on your computer), so if proccessing
     the output takes more than that, you know the board is impossible
    * I don't have any more notes
    * Actually, I do: true winners don't use python programs to solve sudokos, they use
     their head. Although, my motivation for creating this program is to solve a sudoku 
     I had trouble with, so... 
