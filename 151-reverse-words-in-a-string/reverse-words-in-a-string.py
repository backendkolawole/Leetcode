class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = reversed(s.split(' '))
        my_list = [char for char in arr if char]
        s = ' '.join(my_list)
        
        return s
        