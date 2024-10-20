# sort the input array
# declare two pointers i and j with initial value 0 and len(people) - 1
# while the two pointers havent met
# pick up the heaviest person on the boat
# if there is room for another person, pick up that person and move the i pointer forward

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        count = 0

        while (i <= j):
            remain = limit - people[j]
            if (people[i] <= remain):
                i += 1
            count += 1
            j -=1

        return count
