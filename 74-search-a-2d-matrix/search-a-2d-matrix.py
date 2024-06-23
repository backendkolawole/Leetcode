# search for a potential row
# perform binary search on candidate row


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr, val):
            i = 0
            j = len(arr) - 1

            while (i <= j):
                mid = (i + j) // 2

                if (val == arr[mid]):
                    return True
                if (val < arr[mid]):
                    j = mid - 1
                else:
                    i = mid + 1
            
            return False
        
        def isPotentialRow(arr, val):
            i = 0
            j = len(arr) - 1

            return arr[i] <= val <= arr[j]

        i = 0
        j = len(matrix) - 1
        
        while (i <= j):
            mid = (i + j) // 2

            if ( isPotentialRow(matrix[mid], target) ):
                return binarySearch(matrix[mid], target)
        
            if (target < matrix[mid][0]):
                j = mid - 1
            else:
                i = mid + 1