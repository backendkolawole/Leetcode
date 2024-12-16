class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        start_row = 0
        end_row = len(matrix)
        start_column = 0
        end_column = len(matrix[0])

        while (start_row < end_row and start_column < end_column):

            # traverse from left to right
            for i in range(start_column, end_column):
                output.append(matrix[start_row][i])
            
            start_row += 1

            # traverse from top to bottom
            for i in range(start_row, end_row):
                output.append(matrix[i][end_column - 1])
            
            end_column -=1

            if (start_row < end_row):
                # traverse from right to left
                for i in range(end_column - 1, start_column - 1, - 1):
                    output.append(matrix[end_row - 1][i])
                end_row -= 1

            if (start_column < end_column):
                # traverse from bottom to top
                for i in range(end_row - 1, start_row - 1, - 1):
                    output.append(matrix[i][start_column])
                start_column += 1

        return output
        