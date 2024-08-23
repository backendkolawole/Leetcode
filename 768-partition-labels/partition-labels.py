# iterate through string s
# store the last index of each char

# iterate through string s
# declare a variable size which is the size of the current partition
# declare a variable end which is the end index of the current partition
# update the end index
# increment the size
# if the current index is equal to the end index, push the size of partion to result arr

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup = {}
        result = []
        for i in range(len(s)):
            lookup[s[i]] = i

        
        end = 0
        size = 0
        for i, val in enumerate(s):
            end = max(end, lookup[val])
            size +=1
            print(end, size)

            if (end == i):
                result.append(size)
                size = 0
        
        return result