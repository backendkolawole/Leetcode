class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        result = ""

        first = strs[0]

        last = strs[-1]

        for index, char in enumerate(first):
            if (char != last[index]):
                return result
            result += char

        return result
        