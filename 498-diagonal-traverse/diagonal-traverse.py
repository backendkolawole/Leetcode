class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        columns = len(mat[0])
        going_up = True
        result = []
        cur_row = 0
        cur_col = 0

        while (len(result) < rows * columns):
            if (going_up):
                while (cur_row >= 0 and cur_col < columns):
                    result.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1

                if (cur_col == columns):
                    cur_col -= 1
                    cur_row += 2
                
                else:
                    cur_row += 1
                going_up = False
            
            else:
                while (cur_col >= 0 and cur_row < rows):
                    result.append(mat[cur_row][cur_col])
                    cur_col -= 1
                    cur_row += 1
                
                if (cur_row == rows):
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                going_up = True

        
        return result



        