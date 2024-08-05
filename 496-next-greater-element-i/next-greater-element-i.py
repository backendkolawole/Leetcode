class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        lookup = {key: index for index, key in enumerate(nums1)}
        # print(lookup)
        ans = [-1] * len(nums1)

        for i in range(len(nums2) -1, -1, -1):
            current = nums2[i]
            if not stack:
                print('stack is empty', stack, ' inserting ', current)
                stack.append(current)
                continue
                
            while stack and current > stack[-1]:
                stack.pop()
                print(f"popped from stack {stack}")
            if stack:
                if current in lookup:
                    index = lookup[current]
                    ans[index] = stack[-1]
                stack.append(current)
            else:
                stack.append(current)
            
        return ans
                    
