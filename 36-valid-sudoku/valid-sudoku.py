# declare a set variable that will store values in each row, column and box
# iterate through each cell in the matrix row by row
# for each cell in the matrix
# if the current cell is present in the row, or present in the column or present in the box return false
# return true 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set = set()

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if (cell == "."):
                    continue
                # box_index = (3 * (i // 3)) + j // 3
                box_index = 3 * math.floor(i / 3) + math.floor(j / 3)

                row = f"row: ${i}, cell: ${cell}"
                column = f"column: ${j}, cell: ${cell}"
                box = f"box: ${box_index}, cell: ${cell}"
                if (row in my_set or column in my_set or box in my_set):
                    return False
                
                my_set.add(row)
                my_set.add(column)
                my_set.add(box)
        
        return True