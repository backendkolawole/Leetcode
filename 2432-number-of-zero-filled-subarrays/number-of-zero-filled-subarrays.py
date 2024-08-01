class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                result += count + 1
                count +=1
            else:
                count = 0

        return result
