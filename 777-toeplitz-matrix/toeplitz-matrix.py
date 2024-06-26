# define a function isDiagonalUniValue that returns true or false if every cell in the diagonal is the same
# the function takes two dimensions i and j and a prevValue
# while the dimensions are still in bounds 
# if the current element is not equal to the prevValue return false
# else, increment row and column by 1
# iterate through the columns of the grid and call isDiagonaluNI on the cells
# iterate through the grid and call isDiang on the cells
# 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        def isDiagonalUniValue(i, j):
            val = matrix[i][j]

            while (i < rows and j < columns):
                if (val != matrix[i][j]):
                    return False
                i += 1
                j += 1
            return True

        for i in range(columns):
            if not isDiagonalUniValue(0, i):
                return False
        
        for i in range(1, rows):
            if not isDiagonalUniValue(i, 0):
                return False

        return True
            

        