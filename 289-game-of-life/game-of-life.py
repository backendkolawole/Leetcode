# declare a function count neighbor that takes the current cordinates of the cell
# check the neighboring cells of current cell
# return the count of the live no of cells

# iterate through board
# for each cell 
# if the cell is currently live
# if that live cell has less than two neighbors or three neighbors, the cell is going to live on to the next generation
# else the live cell is going to die

# if the cell is currently dead
# if the count of neighbors is equal to 3 the cell lives on to the next generation

# if a cell was alive and is going to die, turn it into a 2
# if a cell was dead and is going to live turn it into a -1

# retransform the board to a normal state so that 2 turns into 0 and -1s turn into a 1

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(-1, 0) , (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        rows = len(board)
        columns = len(board[0])

        def countNeighbors(i, j):
            count = 0
            for x, y in directions:
                if (0 <= i + x <= rows - 1 and 0 <= j + y <= columns - 1):
                    if (board[i + x][j + y] >= 1):
                        count += 1 
            return count
        

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]

                if (cell == 1):
                    count = countNeighbors(i, j)
                    if (count not in [2, 3]):
                        board[i][j] = 2
                elif (cell == 0):
                    count = countNeighbors(i, j)
                    if (count == 3):
                        board[i][j] = -1
        

        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]
                if (cell == -1):
                    board[i][j] = 1
                elif (cell == 2):
                    board[i][j] = 0
        
        return board


        