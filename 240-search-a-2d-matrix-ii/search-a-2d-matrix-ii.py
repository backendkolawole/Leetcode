# take the dimensions of the matrix
# start search at the bottom left of the matrix
# if the target is not present in the current row or not present in the current column
# remove present row or column from search space

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        while (left_col <= right_col and top_row <= bottom_row):
            cell = matrix[bottom_row][left_col]
            if (cell == target):
                return True
            if (target < cell):
                bottom_row -= 1
            elif (target > cell):
                left_col += 1

        return False 
        