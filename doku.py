import sys 

PRINT_OUTPUT = False
OUTPUT_TO_FILE = False
INPUT_FILE = None
SOLVED_BOARD = False
STATISTICS = {
    "ACTIVE" : False,
    "WRITE_TO_FILE" : False,
    "OUTPUT_FILE" : None,
    "START_TIME" : None,
    "ITERATIONS" : 0,
    "OUTPUT_MESSAGE" : "Start time: {}\nEnd time: {}\nTime Delta: {}\nIterations: {}"
}

class BadSudokuException(Exception):
    """
        This class is a custom exception made to indicate that the sudoku is not valid
    """
    pass

def calculate_possibilities(x_pos, y_pos, board):
    """ 
        This function calculates the possible inputs to a given node on the board
        Input:
            x_pos : int = x position of node
            y_pos : int = y position of node
            board : List<List> = a 2d list containing a 3*3 board
        Output:
            possibilities : List = a list containing the possibilities
    """

    possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for x in range(0, 9):
        if x is not x_pos:
            if board[x][y_pos] != "0":
                if board[x][y_pos] in possibilities:
                    possibilities.remove(board[x][y_pos])

    for y in range(0, 9):
        if y is not y_pos:
            if board[x_pos][y] != "0":
                if board[x_pos][y] in possibilities:
                    possibilities.remove(board[x_pos][y])

    x_square = calc_square(x_pos)
    y_square = calc_square(y_pos)
    
    for x in range(x_square[0], x_square[1]):
        for y in range(y_square[0], y_square[1]):
            if (x, y) != (x_pos, y_pos):
                if board[x][y] != "0":
                    if board[x][y] in possibilities:
                        possibilities.remove(board[x][y])

    return possibilities

def calc_square(cordinate):
    """
        This function checks the square of a given coordinate
        Input:
            board : List<List> = a 2d list containing a 3*3 board
        Output:
            Tuple containing min and max ranges based on the square of the coordinate
    """
    if cordinate < 3:
        return (0, 3)
    elif cordinate > 5:
        return (6, 9)
    else:
        return (3, 6)

def check_integrity(board):
    """
    This function checks if the board that was given is valid.
    If it's not, function raises BadSudokuException.

    Input:
        board : List<List> = a 2d list containing a 3*3 board
    Output:
        None
    """
    valid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for x in range(0, 9):
        for y in range(0, 9): 
            if board[x][y] not in valid:
                if __name__ == "__main__":
                    sys.exit("Sudoku has invalid characters")
                else:
                    raise BadSudokuException("Sudoku has invalid characters")

    if len(board) is not 9 or any(len(row) is not 9 for row in board):
        if __name__ == "__main__":
            sys.exit("Sudoku has invalid length")
        else:
            raise BadSudokuException("Sudoku has invalid length")

def boardIsFull(board):
    """
        This function checks if the board is full
         
        Input:
            board : List<List> = a 2d list containing a 3*3 board
        Output:
            Bool - if the board is full or not
    """
    return not any("0" in row for row in board)

def solve(board):
    """
        This function solved a 3*3 sudoku board

        Input:
            board : List<List> = a 2d list containing a 3*3 board
    """

    if boardIsFull(board):
        global PRINT_OUTPUT
        global OUTPUT_TO_FILE
        global SOLVED_BOARD

        SOLVED_BOARD = True
        if PRINT_OUTPUT: 
            print_board(board)
        if OUTPUT_TO_FILE:
            output_to_file(board)

        return
    else:
        global STATISTICS

        STATISTICS["ITERATIONS"] += 1

        x_empty, y_empty = 0, 0
        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] == "0":
                    x_empty, y_empty = x, y
                    break

        possibilities = calculate_possibilities(x_empty, y_empty, board)

        for possibility in possibilities:
            board[x_empty][y_empty] = possibility
            solve(board)

        board[x_empty][y_empty] = "0"

def print_board(board):
    """
        This function prints the board

        Input:
            board : List<List> = a 2d list containing a 3*3 board
    """

    for x in board:
        for y in x:
            print(" %d " % (int(y),), end = "")
        print("")

def open_csv(src):
    """
        This function opens a given csv file and formats it to a 3*3 sudoku board
        Input:
            src : Str = name of the file to open
        Output:
            board : List<List> = a 2d list containing the sudoku board
    """
    board = 0

    try:
        with open(src, "r") as file:
            board = [x.replace(" ", "").split(",") for x in file.read().split("\n")]
    except FileNotFoundError:
        sys.exit("Argument {} is not a file".format(sys.argv[1]))

    return board

def check_flags():
    """
        This function checks the arguments given by the user, and sets flags accordinglyself.

        The flags:
            PRINT_OUTPUT - whether or not to forward the output to STDOUT
            OUTPUT_TO_FILE - file name to output the solved board to in a csv format
            INPUT_FILE - file that contains a 3*3 sudoku board to solve (in a csv format)
    """

    import os.path
    global PRINT_OUTPUT
    global OUTPUT_TO_FILE
    global INPUT_FILE
    global STATISTICS

    if len(sys.argv) > 2:
        arguments = ["-i", "--in", "-o", "--out", "-p", "--print", "-s", "--statistics", "-sf"
                    "--statistics-to-file"
                        ]

        for idx, arg in enumerate(sys.argv):
            if arg == "-i" or arg == "--in":
                try:
                    if os.path.isfile(sys.argv[idx + 1]):
                        INPUT_FILE = sys.argv[idx + 1]
                    else:
                        sys.exit("Argument {} is not a file".format(sys.argv[idx + 1]))
                except IndexError:
                    sys.exit("No input file specified")

            if arg == "-o" or arg == "--out":
                try:
                    if sys.argv[idx + 1] not in arguments:
                        OUTPUT_TO_FILE = sys.argv[idx + 1]
                    else:
                        sys.exit("No output file specified")
                except IndexError:
                    sys.exit("No output file specified")

            if arg == "-p" or arg == "--print":
                PRINT_OUTPUT = True

            if arg == "-s" or arg == "--statistics":
                from datetime import datetime, timedelta

                STATISTICS["ACTIVE"] = True
                STATISTICS["START_TIME"] = datetime.now()

            if arg == "-sf" or arg == "--statistics-to-file":
                from datetime import datetime, timedelta

                STATISTICS["ACTIVE"] = True
                STATISTICS["START_TIME"] = datetime.now()
                STATISTICS["WRITE_TO_FILE"] = True

                try:
                    if sys.argv[idx + 1] not in arguments:
                        STATISTICS["OUTPUT_FILE"] = sys.argv[idx + 1]
                    else:
                        sys.exit("No output file specified for statistics")
                except IndexError:
                    STATISTICS["OUTPUT_FILE"] = OUTPUT_TO_FILE
                    #sys.exit("No output file specified for statistics")

        if not INPUT_FILE or not OUTPUT_TO_FILE:
            sys.exit("Both input and output should be specified")
    else:
        if os.path.isfile(sys.argv[1]):
            PRINT_OUTPUT = True
            INPUT_FILE = sys.argv[1]
        else:
            sys.exit("Argument {} is not a file".format(sys.argv[1]))
          
def output_to_file(board):
    """
        This function outputs the board to a file in a csv format
    """

    global OUTPUT_TO_FILE

    with open(OUTPUT_TO_FILE, "w") as output:
        for row in board:
            output.write(','.join(row) + "\n")

def output_statistics_to_file():
    """
        This function writes the program's statistics to a file
        If a file is specified after -sf, the file is written to specified file.
        If not, it appends the statistics to the output file specified after -o
    """
    global STATISTICS

    if STATISTICS["OUTPUT_FILE"] == OUTPUT_TO_FILE:
        write_mode = "a" 
    else:
        write_mode = "w"

    with open(STATISTICS["OUTPUT_FILE"], write_mode) as output:
        output.write("\n")
        output.write(STATISTICS["OUTPUT_MESSAGE"].format(STATISTICS["START_TIME"], 
                datetime.now(), 
                datetime.now() - STATISTICS["START_TIME"], 
                STATISTICS["ITERATIONS"]))

if __name__ == "__main__":
    check_flags()

    board = open_csv(INPUT_FILE)

    check_integrity(board)
    
    solve(board)

    if STATISTICS["ACTIVE"]:
        from datetime import datetime, timedelta
        STATISTICS["END_TIME"] = datetime.now()

        if STATISTICS["WRITE_TO_FILE"]:
            output_statistics_to_file()
        else:
            print(STATISTICS["OUTPUT_MESSAGE"].format(STATISTICS["START_TIME"], 
                datetime.now(), 
                datetime.now() - STATISTICS["START_TIME"], 
                STATISTICS["ITERATIONS"]))

    if not SOLVED_BOARD:
        raise BadSudokuException("Sudoku is impossible")

