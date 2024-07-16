# quiz.py
# Author: Joey Xie
# Data: July 16th 2024

# Define Constants
VALID_SUDOKU_ROW_COLUMN_NUMBER = 9
INVALID_SUDOKU_ROW_COLUMN_NUMBER = 10
SUDOKU_CELL_VALUE_MIN = 1
SUDOKU_CELL_VALUE_MAX = 9
SUDOKU_CELL_EMPTY_VALUE = 0
BOX_SIZE = 3

GET_VALID_NUMBER_BY_ROW_MODE = 0
GET_VALID_NUMBER_BY_COL_MODE = 1
GET_VALID_NUMBER_BY_BOX_MODE = 2

# quiz 1: reverse list
# input: a list can contain any type of data
# expected output: a list which is reversed from the input list

# first method: use index fast reverse
def reverse_list1(l:list):
    result_l = l[::-1]
    return result_l

# second method: use for loop to append
def reverse_list2(l:list):
    result_l = []
    index = len(l) - 1
    while index >= 0:
        result_l.append(l[index])
        index -= 1
    return result_l

# third method: use for loop to switch inplace
def reverse_list3(l:list):
    left = 0
    right = len(l) - 1
    while right > left:
        temp = l[left]
        l[left] = l[right]
        l[right] = temp
        left += 1
        right -= 1
    return l

# fourth method: use self reverse function
def reverse_list4(l:list):
    l.reverse()
    return l

    
# quiz 2: solve a sudoku game
# input: a matrix with 9 rows and 9 columns, each cell in the matrix is expected to be an integer betwen 1 and 9, other situations are not expected;
# assumptions: the input has to be solvable or invalid, if it is valid but not solvable, the fucntion will return the input as well;
# output: expect a output 9x9 matrix with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9;

# Step1: Check if input matrix is a valid input, if input might be invalid, the function will directlly return input;
def is_blank_cell(value):
    return value is None or value == SUDOKU_CELL_EMPTY_VALUE

def is_filled_cell(value):
    return (type(value) == int) and (value >=SUDOKU_CELL_VALUE_MIN) and (value <= SUDOKU_CELL_VALUE_MAX)

def is_cell_valid(value):
    return is_blank_cell(value) or is_filled_cell(value)

def is_sudoku_valid(matrix):
    if (len(matrix) != VALID_SUDOKU_ROW_COLUMN_NUMBER or len(matrix[0]) != VALID_SUDOKU_ROW_COLUMN_NUMBER):
        return False
    for row in range(VALID_SUDOKU_ROW_COLUMN_NUMBER):
        for column in range(VALID_SUDOKU_ROW_COLUMN_NUMBER):
            if (not is_cell_valid(matrix[row][column])):
                return False  
    return True

# Step2: Find Empty cell to filled, and find out how many possible choices for this empty cell;
def find_empty_cell(matrix):
    for row in range(VALID_SUDOKU_ROW_COLUMN_NUMBER):
        for column in range(VALID_SUDOKU_ROW_COLUMN_NUMBER):
            if is_blank_cell(matrix[row][column]):
                return row, column
    return INVALID_SUDOKU_ROW_COLUMN_NUMBER, INVALID_SUDOKU_ROW_COLUMN_NUMBER

def get_values_by_mode(matrix, cur_row, cur_column, mode):
    valid_numbers =[]
    cur_using_numbers = []
    if mode == GET_VALID_NUMBER_BY_BOX_MODE:
        row_num = cur_row // BOX_SIZE
        col_num = cur_column // BOX_SIZE
        for row_index in range(BOX_SIZE):
            for column_index in range(BOX_SIZE):
                cur_value = matrix[row_num * BOX_SIZE + row_index][col_num * BOX_SIZE + column_index]
                if is_blank_cell(cur_value):
                    continue
                cur_using_numbers.append(cur_value)

    else:
        for index in range(VALID_SUDOKU_ROW_COLUMN_NUMBER):
            if mode == GET_VALID_NUMBER_BY_ROW_MODE:
                cur_value = matrix[cur_row][index]
            if mode == GET_VALID_NUMBER_BY_COL_MODE:
                cur_value = matrix[index][cur_column]            
            if is_blank_cell(cur_value):
                continue
            cur_using_numbers.append(cur_value)
    for value in range(SUDOKU_CELL_VALUE_MIN, SUDOKU_CELL_VALUE_MAX + 1):
        if value not in cur_using_numbers:
            valid_numbers.append(value)
    return valid_numbers

def get_filling_values(matrix, cur_row, cur_column):
    row_values = get_values_by_mode(matrix, cur_row, cur_column, GET_VALID_NUMBER_BY_ROW_MODE)
    column_values = get_values_by_mode(matrix, cur_row, cur_column, GET_VALID_NUMBER_BY_COL_MODE)
    box_values = get_values_by_mode(matrix, cur_row, cur_column, GET_VALID_NUMBER_BY_BOX_MODE)

    comm_values = []
    for poss_value in range(SUDOKU_CELL_VALUE_MIN, SUDOKU_CELL_VALUE_MAX + 1):
        if (poss_value in row_values) and (poss_value in column_values) and (poss_value in box_values):
            comm_values.append(poss_value)
    return comm_values


# step3: solave sudoku using recursion, stops only when there is not any empty cell, if there is empty cell but no numbers to fill, function return to last stack and try another possible numbers;
def is_sudoku_solved(matrix):
    target_row, target_column = find_empty_cell(matrix)
    if (target_row == INVALID_SUDOKU_ROW_COLUMN_NUMBER) and (target_column == INVALID_SUDOKU_ROW_COLUMN_NUMBER):
        return True
    filling_values = get_filling_values(matrix, target_row, target_column)
    for value in filling_values:
        matrix[target_row][target_column] = value
        if (is_sudoku_solved(matrix)):
            return True
        matrix[target_row][target_column] = SUDOKU_CELL_EMPTY_VALUE
    return False

# step4: main function
def solve_sudoku(matrix):
    if (not is_sudoku_valid(matrix)):
        return matrix
    if is_sudoku_solved(matrix):
        print("Matrix is solved!")
    else:
        print("Matrix can not be solved.")
    return matrix
    



