# declare a lookup variable that will store the freq of cordinates
# declare a variable max that will hold the largest possible overlap
# iterate over both images and store their cordinates in tuple pairs
# iterate over both list of tuples
# if the difference is present in the lookup object increment it and update the max
# else add it to the lookup table

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        lookup = {}
        largest = 0
        rows = len(img1)
        columns = len(img1[0])
        list1 = []
        list2 = []

        for i in range(rows):
            for j in range(columns):
                if img1[i][j] == 1:
                    list1.append((i, j))
                if img2[i][j] == 1:
                    list2.append((i, j))

        for i, j in list1:
            for x, y in list2:
                translation = (i - x, j - y)
                if not translation in lookup:
                    lookup[translation] = 0
                lookup[translation] += 1
                largest = max(largest, lookup[translation]) 

        return largest


                
        