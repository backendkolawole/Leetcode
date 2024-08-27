# use sliding window approach
# if the basket contains more than 2 elements, start removing fruits from the basket
# add a fruit to the basket
# update the count of fruits in the basket
# return the max count of fruits

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        lookup = {}
        count = 0
        length = 0

        while j < len(fruits):
            if (fruits[j] not in lookup):
                lookup[fruits[j]] = 0
            lookup[fruits[j]] += 1

            while (len(lookup) > 2):
                if (lookup[fruits[i]] == 1):
                    del lookup[fruits[i]]
                else:
                    lookup[fruits[i]] -=1
                i +=1
            
            length = max(length, j - i + 1)
            j += 1
        

        return length
        