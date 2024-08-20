class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        size = len(s)
        low = 0
        high = size
        output = [None] * (size + 1)
        
        for index in range(size):
            if (s[index] == 'I'):
                output[index] = low
                low += 1
            else:
                output[index] = high
                high -=1
        
        output[size] = low
        return output