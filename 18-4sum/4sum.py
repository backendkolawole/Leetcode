class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        my_set = set()
        output = []

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1

                while (c < d):
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    
                    if (sum == target):
                        values = (nums[a], nums[b], nums[c], nums[d])
                        if values not in my_set:
                            my_set.add(values)
                            output.append([nums[a], nums[b], nums[c], nums[d]])        
                        c += 1
                        d -= 1
                    elif (sum < target):
                        c += 1
                    else:
                        d -= 1
        
        return output