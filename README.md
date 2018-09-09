# Duko.py is a 3*3 Sudoku solving Python program, enabled by Big Data and AI (Totally not backtracking and recursion)

**The file doku.py was written by F4dora_0f_d00m.
If you want access to make changes to this repository, ask questiosn or 
give any sort of feedback, be free to contact me.**

**This Python file is free for all to use. If you find it useful somehow,
be sure to tell me**


# User's Guide #
Currently, only .csv files are supported. Make sure the files are formatted like in the example files.
The program was written with Python3 in mind.

### Standard I/O ###

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
### Statistics ###

Stastics include:
    1. Start time
    2. End Time
    3. Time Delta
    4. Number of iterations

Currently, statistics come in two flavours: statistics that are presented on screen, and
statistics that are written to a file.

To just view statistics, add the ```-s``` flag or the ```--statistics``` flag to the program input.
Example:
```
    python3 doku.py -i [csv file containing the board] -o [name of the outputfile] -s
```
   Alternatively, you can use:
```
    python3 doku.py --in [csv file containing the board] -out [name of the outputfile] --statistics
```

If you want to output the statistics onto a file, add the ```-sf``` flag or the```--statistics-to-file``` 
flag to the program input. After the flag, you can specify a file to write the statistics to. If a new file
is not specified, the statistics will be appended to the file specified after out.

Example:
```
    python3 doku.py -i input.csv -o output -sf
```
This command will write the statistics to the file "output"
```
    python3 doku.py -input.csv -o output -sf stats_output
```
This command will write the statistics to the file "stats_output"

### A few notes: ###
true winners don't use python programs to solve sudokos, they use
their head. Although, my motivation for creating this program was to solve a sudoku 
I had trouble with, so... 
