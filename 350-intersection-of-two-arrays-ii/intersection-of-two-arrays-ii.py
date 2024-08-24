class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        result = []
        
        for item in nums1:
            if item not in lookup:
                lookup[item] = 0
            lookup[item] += 1

        for item in nums2:
            if item in lookup and lookup[item]:
                result.append(item)
                lookup[item] -= 1
        
        return result
        