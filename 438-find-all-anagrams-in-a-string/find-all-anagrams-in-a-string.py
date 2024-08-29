class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        if (len(s) < len(p)):
            return output
        pCount = Counter(p)
        sCount = Counter(s[:len(p)])

        output = [0] if (sCount == pCount) else []
        l = 0
        
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if (sCount[s[l]] == 0):
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                output.append(l)
        
        return output

