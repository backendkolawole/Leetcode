# get the dimensions
# declare a variable result which will be the result array
# while the indices are still in bound

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # rows = len(matrix)
        # columns = len(matrix[0])
        output = []
        top_row = 0
        bottom_row = len(matrix)
        left_col = 0
        right_col = len(matrix[0]) 


        while (left_col < right_col and top_row < bottom_row):

            # traverse left to right
            for i in range(left_col, right_col):
                output.append(matrix[top_row][i])
            
            top_row += 1


            # traverse top to bottom
            for i in range(top_row, bottom_row):
                output.append(matrix[i][right_col - 1])
            right_col -=1


            # traverse right to left

            if (top_row < bottom_row):
                for i in range(right_col - 1, left_col - 1, -1):
                    output.append(matrix[bottom_row - 1][i])
                bottom_row -=1

            # traverse bottom to the top
            if (left_col < right_col):
                for i in range(bottom_row - 1, top_row - 1, - 1):
                    output.append(matrix[i][left_col])
                left_col += 1

        return output