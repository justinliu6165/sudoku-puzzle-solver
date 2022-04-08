import math

# Set up sudoku puzzle (REF: sudoku_puzzle.png)
# 0 is equal to an empty cell
sudoku_pizzle = [
    [0,4,0,0,0,0,8,6,6],
    [6,0,0,5,8,0,3,0,0],
    [3,5,0,7,4,0,0,2,0],
    [0,0,5,8,1,0,2,0,0],
    [0,7,0,3,9,0,5,8,0],
    [9,8,1,0,6,0,7,0,3],
    [0,0,0,4,7,0,0,5,0],
    [0,0,7,0,5,0,0,0,2],
    [0,2,4,6,3,0,0,0,0],
]

potentials = {}

def check_cell(x,y):
    # Function checks the potential values in empty spaces
    if sudoku_pizzle[y][x] != 0: return
    
    available_digits = list(range(1, 10))
    
    # Check row values:
    for idx, cell in enumerate(sudoku_pizzle[y]):
        if len(available_digits) == 1: break
        
        if idx != x:
            if cell in available_digits: available_digits.remove(cell)
    
    # Check column values:
    for idx, row in enumerate(sudoku_pizzle):
        if len(available_digits) == 1: break
        
        cell = row[x]
        if idx != y:
            if cell in available_digits: available_digits.remove(cell) 
            
    # Check 3x3 grid:
    base = 3
    cell_x_start = base * math.floor(x/base)
    cell_x_end = cell_x_start + base
    cell_y_start = base * math.floor(y/base)
    cell_y_end = cell_y_start + base
    
    for min_cell_y in range(cell_y_start, cell_y_end):
        if len(available_digits) == 1: break
        
        for min_cell_x in range(cell_x_start, cell_x_end):
            if len(available_digits) == 1: break
            
            cell = sudoku_pizzle[min_cell_y][min_cell_x]
            if cell in available_digits: available_digits.remove(cell) 
    
    if len(available_digits) > 1:
        potentials[str(x) + str(y)] = available_digits
        return False
    else:
        if (str(x) + str(y)) in potentials:
            del potentials[str(x) + str(y)]
        return available_digits[0]
    
def update_grid(x,y,val):
    sudoku_pizzle[y][x] = val
    
def check_for_empty_cells():
    tmp_matrix = sudoku_pizzle
    for row in tmp_matrix:
        if 0 in row:
            return True
    return False
        
    
def loop_sudoku_puzzle():
    for x, row in enumerate(sudoku_pizzle):
        for y, cell in enumerate(row):
            if cell == 0:
                new_val = check_cell(x,y)
                if new_val != False:
                    update_grid(x,y,new_val)
                    break
        break
    if check_for_empty_cells():
        loop_sudoku_puzzle()

# loop_sudoku_puzzle()

for row in sudoku_pizzle:
    print(row)