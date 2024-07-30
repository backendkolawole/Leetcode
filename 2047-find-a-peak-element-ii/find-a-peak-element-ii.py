# take the dimensions of the grid
# declare two cordinate variable i and j with initial value 0
# while in bound 
# check all adjacent neighbors of the current cell 
# if the neighbor is greater than the current cell 
# reduce the search space
# else return the current cell
# return -1 if the 

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        columns = len(mat[0])
        i = 0
        j = 0

        while i < rows and j < columns:
            if i - 1 >= 0 and mat[i - 1][j] > mat[i][j]:
                i -= 1
            elif j + 1 < columns and mat[i][j + 1] > mat[i][j]:
                j += 1
            elif i + 1 < rows and mat[i + 1][j] > mat[i][j]:
                i += 1
            elif j - 1 >= 0 and mat[i][j - 1] > mat[i][j]:
                j -= 1
            else:
                return [i, j]

