class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)

        ans = [-1] * length

        for i in range((length * 2) -1, -1, -1):
            current = nums[i % length]
            if not stack:
                stack.append(current)

            while stack and current >= stack[-1]:
                stack.pop()
            if stack:
                ans[i % length] = stack[-1]
                stack.append(current)
            else:
                stack.append(current)

        return ans