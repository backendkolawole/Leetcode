class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        result = 0
        total = 0

        for i, val in enumerate(nums):
            # print(lookup)
            total += val
            remainder = (total % k + k) % k

            if (remainder not in lookup):
                lookup[remainder] = 0
            else:
                result += lookup[remainder]
            lookup[remainder] +=1

        
        return result
