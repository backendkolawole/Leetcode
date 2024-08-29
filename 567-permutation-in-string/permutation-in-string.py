class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1Count = Counter(s1)
        s2Count = Counter(s2[:window_size])
        
        if (s1Count == s2Count): return True

        l = 0
        for r in range(window_size, len(s2)):
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            if s2Count[s2[l]] == 1:
                s2Count.pop(s2[l])
            else:
                s2Count[s2[l]] -= 1
            
            l+=1
            if s1Count == s2Count:
                return True
            
        return False
