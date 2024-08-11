class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        my_list = [char for char in s.split(' ') if char]
        arr = reversed(my_list)
        s = ' '.join(arr)
        
        return s
        