class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        my_list = [char for char in s.split(' ') if char]
        # arr = reversed(my_list)
        my_list.reverse()
        # print(arr, my_list.reverse())
        s = ' '.join(my_list)
        
        return s
        