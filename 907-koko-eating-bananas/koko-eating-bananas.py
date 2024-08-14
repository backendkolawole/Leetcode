# use bs search
# declare two boundary variables i and j with initial values 1 and the max pile in the list of bananas
# choose a speed
# if koko can eat all the bananas at current speed
# choose a lessser speed

# else choose a greater speed
# define a function can eat that returns true if the piles can be eaten at current speed
# iterate through piles
# calculate the total times
# return true if the total time taken is less than the number of hours

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)

            return hours <= h 

        i = 1
        j = max(piles)

        while (i <= j):
            speed = (i + j) // 2
            
            if (canEat(speed)):
                j = speed - 1
            else:
                i = speed + 1

        
        return i