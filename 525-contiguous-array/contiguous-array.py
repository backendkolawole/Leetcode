class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0: -1}
        count = 0
        max_length = 0

        for index, val in enumerate(nums):
            if (val == 0): count -= 1
            else: count +=1

            if count not in lookup:
                lookup[count] = index
            else:
                max_length = max(max_length, index - lookup[count])

        
        return max_length
