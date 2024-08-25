class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        lookup = {0: -1}

        for index, val in enumerate(nums):
            total += val
            remainder = total % k

            if (remainder not in lookup):
                lookup[remainder] = index
            elif index - lookup[remainder] > 1:
                return True
        
        return False

        