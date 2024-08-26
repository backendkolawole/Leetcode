class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        count = 0
        total = 0

        for i, val in enumerate(nums):
            total += val
            sum = total - k

            if (sum in lookup):
                count += lookup[sum]
            
            if (total not in lookup):
                lookup[total] = 0
            lookup[total] += 1

        return count
        