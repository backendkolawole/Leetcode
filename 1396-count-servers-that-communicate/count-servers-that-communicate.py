# declare two lookup tables that will count the number of servers in each row and columns
# iterate throught the grid
# if the current server has more than one server in its row or column, increment the count of servers
# return the count of servers

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        row_count = {}
        column_count = {}
        servers = 0

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 1):
                    if (i not in row_count):
                        row_count[i] = 0
                    row_count[i] +=1

                    if (j not in column_count):
                        column_count[j] = 0
                    column_count[j] += 1

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]

                if (cell == 1):
                    if (row_count[i] > 1 or column_count[j] > 1):
                        servers += 1

        return servers
                
        
        