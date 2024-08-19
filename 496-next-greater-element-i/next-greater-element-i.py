class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        lookup = {key: index for index, key in enumerate(nums1)}
        ans = [-1] * len(nums1)

        for i in range(len(nums2) -1, -1, -1):
            current = nums2[i]
            if not stack:
                stack.append(current)
                
            while stack and current >= stack[-1]:
                stack.pop()
            if stack:
                if current in lookup:
                    index = lookup[current]
                    ans[index] = stack[-1]
            stack.append(current)

            
        return ans
                    