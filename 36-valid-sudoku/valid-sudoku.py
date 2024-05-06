# iterate through the board row by row
# for each cell in the board,
# if the current cell is present in the the set of rows return false, else add it to the set of rows
# repeat the same process for columns and subboxes
# return true at the end of the iteration

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        columns = len(board[0])
        my_set = set()

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]
                box_index = (3 *  math.floor(i / 3)) + math.floor(j / 3)

                if (cell != '.'):
                    row = f"row: {i}, cell: {cell}"
                    column = f"column: {j}, cell: {cell}"
                    sub_box = f"sub_box: {box_index}, cell: {cell}"
                    print(row)

                    if (row in my_set or column in my_set or sub_box in my_set):
                        return False
                    my_set.add(row)
                    my_set.add(column)
                    my_set.add(sub_box)
        
        return True

        