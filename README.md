# Sudoku puzzle automatic solver

Console-based application that solves sudokus

## Procedure
1. Loop through each cell, determine if empty
2. Check what numbers are valid 
    - Check row for numbers
    - Check column for numbers
    - Check small grid (3x3) the cell is in
3. If single value found, update sudoku puzzle
4. Loop through the cells again, repeat procedure

This is a very simple way to update the sudoku, however some issues may arise through this method. When looping through, when no cell is found to have a single value, it could create an infinite loop.

## Assumptions
Sudoku is passed set up as a 2D array matrix
```
sudoku_puzzle = [
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
```


## Next steps
1. Find a way to loop through until all 0 cells are gone
2. Improve algorithm to reduce iterations / time taken