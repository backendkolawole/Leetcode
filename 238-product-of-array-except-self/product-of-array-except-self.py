class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [None] * len(nums)
        right = [None] * len(nums)
        left_multiply = 1
        right_multiply = 1

        for i in range(len(nums)):
            left[i] = left_multiply
            left_multiply *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            right[i] = right_multiply * left[i]
            right_multiply *= nums[i]

        return right
        