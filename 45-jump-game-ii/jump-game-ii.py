class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        farthest = 0
        landing_position = 0
        destination = len(nums) - 1

        if (len(nums) == 1):
            return 0

        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)

            if (i == landing_position):
                landing_position = farthest
                jumps+=1

                if (farthest >= destination):
                    return jumps
            
        
        return jumps