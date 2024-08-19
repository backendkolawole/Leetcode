class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        result = [None] * len(nums)

        for num in nums:
            if (num % 2 == 0):
                result[even] = num
                even += 2
            else:
                result[odd] = num
                odd += 2

        
        return result