class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals) == 1):
            return intervals
        intervals = sorted(intervals, key=lambda x: x [0])

        new_interval = intervals[0]
        result = [new_interval]

        for interval in intervals:
            if (interval[0] <= new_interval[1]):
                new_interval[1] = max(interval[1], new_interval[1])
            
            else:
                new_interval = interval
                result.append(new_interval)


        return result