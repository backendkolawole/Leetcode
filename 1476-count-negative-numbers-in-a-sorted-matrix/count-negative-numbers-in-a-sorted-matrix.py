# return the count of numbers that are negative in a sorted grid
# take the dimensions of the grid
# declare two starting variables i and j with initial values 0 and columns 
# declare a variable count that we will return
# while i is less than or equal to rows and j is greater than or equal to 0
# if the element at the current cordinates is a positive number, increment the row by 1 because every other number in that row is going to be positive 
# else if the number at the current cordinate is negative, 
# increment count by row minus i
# decrement the j cordinate by 1 because every other number in that column is negative, 
# 

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        i = 0
        j = columns - 1
        count = 0

        while i <= rows - 1 and j >= 0:
            if (grid[i][j] < 0):
                count += rows - i
                j -= 1
            
            else:
                i += 1
        

        return count
        