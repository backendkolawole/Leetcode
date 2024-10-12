class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)

        def reverse(arr, i, j):
            
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        reverse(nums, i = 0, j = len(nums) - 1)
        reverse(nums, i = 0, j = k - 1)
        reverse(nums, i = k, j = len(nums) - 1)
        