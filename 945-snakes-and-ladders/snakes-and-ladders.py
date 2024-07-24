# declare a variable coordinates that will hold the cell coordinates in the board
# declare a variable queue that will hold the next destination in the traversal
# while the queue is not empty
# pop the current position from the queue
# if the current position is the square n*n, return the min moves it took to get to current positon
# choose a destination square next in the range [curr + 1, min(curr + 6, n2)],
# get the coordinates of the next destination
# if the next destination has a snake or ladder, move to the destination of that snake or ladder
# if we have not previously reached the destination cell, 
# push the next destination into the queue 
# update the minmoves it took to get to the next the next destionation

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        coordinates = [None] * ((n * n) + 1)
        label = 1
        
        for i in range(n - 1, -1, -1):
            if (n - i) % 2 == 1:
                for j in range(n):
                    coordinates[label] = (i, j)
                    label += 1
            else:
                for j in range(n - 1, -1, -1):
                    coordinates[label] = (i, j)
                    label += 1

        min_moves = [-1] * ((n * n) + 1)
        min_moves[1] = 0
        queue = [1]
        
        while (queue):
            curr = queue.pop(0)
            if (curr == n * n):
                return min_moves[curr]

            for next in range(curr + 1, min(curr + 6, n * n) + 1):
                i, j = coordinates[next]
                destination = next

                if board[i][j] != -1:
                    destination = board[i][j]
                if min_moves[destination] == -1:
                    queue.append(destination)
                    min_moves[destination] = min_moves[curr] + 1

        return -1
            