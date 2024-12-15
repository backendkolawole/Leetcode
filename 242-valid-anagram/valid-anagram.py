class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        lookup = {}

        for char in s:
            if char not in lookup:
                lookup[char] = 0
            lookup[char] += 1
        

        for char in t:
            if (char not in lookup or lookup[char] <= 0):
                return False
            lookup[char] -= 1

        return True
        