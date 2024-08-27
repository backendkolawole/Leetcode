class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def isOdd(num):
            return num % 2 != 0

        for i in range(len(nums)):
            if isOdd(nums[i]): nums[i] = 1
            else: nums[i] = 0

        i = 0
        j = 0
        total = 0
        count = 0
        lookup = {0: 1}

        while (j < len(nums)):
            total += nums[j]

            sum = total - k

            if (sum in lookup):
                count += lookup[sum]
            
            if total not in lookup:
                lookup[total] = 0
            lookup[total] += 1

            j += 1
        
        return count