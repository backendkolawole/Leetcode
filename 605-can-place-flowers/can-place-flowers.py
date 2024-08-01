# iterate through the flowerbed
# if the current bed is empty
# if the leftplot is free and its rightplot is free,
# plant a flower in the current plot
# decrement the count of n
# if n is equal to 0 return true
# return false outside the loop

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if (n == 0):
            return True
        
        for i in range(len(flowerbed)):
            isEmptyLeftPlot = i == 0 or flowerbed[i - 1] == 0
            isEmptyRightPlot = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0 

            # print(isEmptyLeftPlot, isEmptyRightPlot)
            if (flowerbed[i] == 0):
                if isEmptyLeftPlot and isEmptyRightPlot:
                    n -=1
                    flowerbed[i] = 1
                    if (n == 0):
                        return True
        
        return False