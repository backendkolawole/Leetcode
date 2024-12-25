class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        lookup = {}
        result = []


        while (i <= len(s) - 9):
            substring = s[i: i + 10]

            if (substring not in lookup):
                lookup[substring] = 0
            
            lookup[substring] += 1

            if (lookup[substring] == 2):
                result.append(substring)
            
            i += 1
        
        return result

        