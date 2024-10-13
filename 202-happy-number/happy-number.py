class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()

        while n:
            n = str(n)
            sum = 0

            for char in n:
                sum += int(char)**2
            
            if (sum == 1):
                return True
            if (sum in my_set):
                return False
            my_set.add(sum)

            n = sum
        
        return False
        