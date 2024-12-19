class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        fresh = 0
        queue = []

        for i in range(rows):
            for j in range(columns):
                cell = grid[i][j]
                if (cell == 1):
                    fresh += 1
                elif (cell == 2):
                    queue.append((i, j))

        def isValid(i, j):
            if (i < 0 or j < 0 or i == rows or j == columns or grid[i][j] != 1):
                return False
            return True
            
        minutes = 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while (queue and fresh > 0):
            size = len(queue)

            for i in range(size):
                x, y = queue.pop(0)
                
                for a, b in directions:
                    new_x = a + x
                    new_y = b + y

                    if (isValid(new_x, new_y)):
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                        fresh -= 1
                
            minutes +=1
        
        return minutes if fresh == 0 else -1
                