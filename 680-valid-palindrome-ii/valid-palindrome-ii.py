class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(word):
            i = 0
            j = len(word) - 1

            while (i < j):
                if (word[i] != word[j]):
                    return False
                i += 1
                j -=1
            
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if (s[i] != s[j]):
                return isPalindrome(s[:i] + s[i+1:]) or isPalindrome(s[:j] + s[j + 1:])
            i += 1
            j -=1

        
        return True