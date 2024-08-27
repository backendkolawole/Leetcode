class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # find the subarray with maximum sum that has unique elements

        i = 0
        j = 0
        my_set = set()
        result = 0
        sum = 0

        while (j < len(nums)):

            while (nums[j] in my_set):
                sum -= nums[i]
                my_set.remove(nums[i])
                i += 1
            
            sum += nums[j]
            result = max(result, sum)
            my_set.add(nums[j])
            j +=1

        
        return result