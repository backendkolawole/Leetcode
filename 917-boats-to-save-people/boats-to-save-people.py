class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        result = 0

        while (i <= j):
            remain = limit - people[j]
            result += 1
            j -= 1

            if (i <= j) and people[i] <= remain:
              i += 1

        return result  