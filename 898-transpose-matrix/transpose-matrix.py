# declare a new matrix with reverse dimensions
# iterate through the matrix and flip its row and columns

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        result = [[None] * rows for _ in range(columns) ]
        
        for i in range(rows):
            for j in range(columns):
                result[j][i] = matrix[i][j] 

        return result
        