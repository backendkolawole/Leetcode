class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(' ') if word]
        
        i = 0
        j = len(words) - 1

        while (i < j):
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        
        return ' '.join(words)
        