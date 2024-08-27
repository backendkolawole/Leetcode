class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if (k <= 1):
            return 0
        i = 0
        j = 0
        product = 1
        count = 0

        while (j < len(nums)):
            cur = nums[j]

            product *= cur

            while (product >= k):
                product /= nums[i]
                i +=1
            
            count += j - i + 1
            j+=1
        
        return count
        