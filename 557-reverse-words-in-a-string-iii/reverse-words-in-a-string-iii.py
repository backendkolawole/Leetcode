class Solution:
    def reverseWords(self, s: str) -> str:

        def reverseWord(char):
            word = [c for c in char]
            i = 0
            j = len(word) - 1

            while (i < j):
                word[i], word[j] = word[j], word[i]
                i +=1
                j -=1
            
            return ''.join(word)

        my_list = [reverseWord(word) for word in s.split(' ')]

        return ' '.join(my_list)
        