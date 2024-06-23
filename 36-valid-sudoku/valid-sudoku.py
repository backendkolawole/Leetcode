# the sudoku board is valid if each row, column and subbox contain unique elements
# declare three set variables rows. columns and subbx
# iterate through the board
# if the current cell is already present in a row, column or subbox return false
# else put it in 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set = set()
        rows = len(board)
        columns = len(board[0])


        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]
                box_index = (3 *  math.floor(i / 3)) + math.floor(j / 3)

                if (cell != '.'):
                    row = f"row: {i}, cell: {cell}"
                    column = f"column: {j}, cell: {cell}"
                    sub_box = f"sub_box: {box_index}, cell: {cell}"
                    if (row in my_set or column in my_set or sub_box in my_set):
                        return False
                    my_set.add(row)
                    my_set.add(column)
                    my_set.add(sub_box)
            
        return True
                

        