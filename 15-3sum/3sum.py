# take the current element 
# run twosum on the rest of the array

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        lookup = set()
        nums.sort()

        for i in range(len(nums) - 2):
            first = nums[i]
            a = i + 1
            b = len(nums) - 1

            while (a < b):
                sum = first + nums[a] + nums[b]
                if (sum == 0):
                    value = (first, nums[a], nums[b])
                    if value not in lookup:
                        lookup.add(value)
                        output.append([first, nums[a], nums[b]])
                    a += 1
                    b -= 1
                elif (sum < 0):
                    a += 1
                else:
                    b -= 1

        return output