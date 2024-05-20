class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        
        # dict for transition rule
        rules = {
            1: {0: 0, 3: 3},
            2: {1: 1, 2: 2},
            3: {0: 2, 1: 3},
            4: {1: 0, 3: 2},
            5: {0: 1, 2: 3},
            6: {2: 0, 3: 1},
        }
        
        # dict for update rule
        moves = {
            0: (0, 1),
            1: (-1, 0),
            2: (1, 0),
            3: (0, -1),
        }
        
        i, j = (0, 0)
        k = grid[0][0]
        d = list(rules[k].keys())
        direction_1 = d[0]
        direction_2 = d[1]
        # print(d)
        
        # define a variable set that keeps track of visited coordinates to detect loops and checks if the bottom-right corner of the grid is reached. 
        # If a valid path is found in either of the two possible starting directions, 
        # the function returns True; otherwise, it returns False.

        def walkMaze(i, j, d):
            # visited = set([(i, j)])
            visited = set((i, j))
            print(visited)

            while True:
                if i < 0 or i >= rows or j < 0 or j >= columns:
                    return False
                
                k = grid[i][j]
                if d not in rules[k]:
                    return False
                
                if (i, j) == (rows - 1, columns - 1):
                    return True
                
                d = rules[k][d]
                i, j = (i + moves[d][0], j + moves[d][1])
                if (i, j) in visited: # there is a loop
                    return False
                visited.add((i, j))
        
        return walkMaze(i, j, direction_1) or walkMaze(i, j, direction_2)
        