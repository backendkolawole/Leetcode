# sort the points by their ending values
# declare a variable arrows which is the count of arrows needed to burst balloons
# declare a variable prev with initial value negative infinity
# iterate through the points
# if the current points start value is greater than prev, increment the count of arrows
# update prev to equal the end value of current point


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        
        arrows = 0
        prev = float(-inf)
        
        for point in points:
            if (point[0] > prev):
                arrows += 1
                prev = point[1]


        return arrows


        