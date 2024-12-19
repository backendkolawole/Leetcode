# take the dimension of the grid
# if the cell at the top-left or bottom right is not equal to a 0, return -1
# declare a variable queue that will hold the cordinates and the path of the elements in the traversal
# while the queue is not empty, take the length of the queue
# in the range length
# pop out the current cordinates and path length from the queue
# if the current cordinates point to the bottom right cell return the path
# add the cordinates and path length of all the valid adjacent cells to the queue
# increment the path length outside of the for loop
# return -1 outside the while loop

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        queue = [(0, 0, 1)]
        visited = set()

        def isValid(i, j):
            if i < 0 or j < 0 or i == n or j == n or grid[i][j] != 0 or (i, j) in visited:
                return False
            return True

        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1] ]
        while queue:
            size = len(queue)

            for _ in range(size):
                r, c, path_length = queue.pop(0)
                if r == len(grid) -1 and c == len(grid[0]) -1:
                    return path_length
                for dr, dc in directions:
                    row = dr + r
                    column = dc + c

                    if (isValid(row, column)):
                        queue.append([row, column, path_length + 1])
                        visited.add((row, column))
                    
        return -1
                

                

        