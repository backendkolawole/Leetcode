# declare a variable sum that will be the matrix diagonal sum
# declare a set variable that will keep track of seen cordinates
# if the current cell is on the primary diagonal or secondary diagonal and not in the set add the cell value to the sum and put the cordinates in a set
# define a function isprimaryDiagonal that takes in a row and column as parameters and returns true if the row and columns are the same
# define a function isSecondaryDiagonal that takes in a row and column and returns true if the sum of the row index and the column index is equal to one less than the total number of columns in the mat.
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cordinates = set()
        sum = 0
        rows = len(mat)
        columns = len(mat[0])

        def isPrimaryDiagonal(i, j):
            return i == j

        def isSecondaryDiagonal(i, j):
            return (i + j) == columns - 1

        for i in range(rows):
            for j in range(columns):
                cell = mat[i][j]

                if isPrimaryDiagonal(i, j) or isSecondaryDiagonal(i, j) and (i, j) not in cordinates:
                    print(cell, i, j, sum)
                    sum += cell
                cordinates.add((i, j))

        return sum

        

        