class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        output = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            output = max(window_sum, output)

        return output / k
        