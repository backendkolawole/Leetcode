# declare a variable visited that will hold the cordinates of the visited cells
# declare a variable queue that will hold the cordinates of the cells in the first island
# take the dimensions of the grid
# iterate through the grid row by row
# if the current cell is a 1      
# run a dfs on the cell and push the cordinates of the cell to the queue and to the visited set
# run a bfs on the cell to find the shortest bridge to connect two islands

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def isValid(i, j):
            if i < 0 or j < 0 or i == n or j == n or (i, j) in visited:
                return False
            return True
        
        visited = set()
        queue = []

        def dfs(i, j):
            if not isValid(i, j) or not grid[i][j]:
                return 
            visited.add((i, j))
            queue.append((i, j))
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            
        
        def bfs():

            bridge = 0
            while queue:
    
                length = len(queue)
                for i in range(length):
                    x, y = queue.pop(0)

                    for dr, dc in directions:
                        new_x = dr + x
                        new_y = dc + y

                        if not isValid(new_x, new_y):
                            continue
                        if grid[new_x][new_y]:
                            return bridge

                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                    
                bridge +=1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()