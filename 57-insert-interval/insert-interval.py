# declare a variable output that will be returned
# iterate through the intervals
# if the end value of the new interval is less than the start of the current interval, insert the new interval into the output array and return the concatenated output
# else if the start of the new interval is greater than the end of the current interval,
# update the new interval
# push the new interval into the output array at the end of the iteration

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        output.append(newInterval)
        return output
