# sort the input string
# iterate through dictionary

# check if the current string can be formed by deleting characters from string s
# if true
# if the size of the current string is greater than the size of the result string, 
# update the result string
# if the size of the current string is equal to the result string, update the result based on lexicographical order


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""

        def canForm(char, target):
            i = 0
            j = 0

            while i < len(char) and j < len(target):
                if (char[i] == target[j]):
                    i += 1
                    j += 1
                else:
                    i+=1
            
            return j == len(target)


        for string in dictionary:
            if(canForm(s, string)):
                size = len(string)
                if (size > len(result)):
                    result = string
                elif (size == len(result)):
                    result = result if result < string else string

        return result
