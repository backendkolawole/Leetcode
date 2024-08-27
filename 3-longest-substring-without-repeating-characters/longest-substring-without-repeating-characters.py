# declare two pointer variables i and j with intiial values 0
# iterate through the string
# if the current substring is unique, expand the window
# else if the current substring is no longer unique, 
# delete elements from our set and our current substring


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        my_set = set()
        length = 0

        while (j < len(s)):
            while (s[j] in my_set):
                my_set.remove(s[i])
                i += 1
            my_set.add(s[j])
            length = max(length, j - i + 1)
            
            j +=1
        
        return length
            

            

        