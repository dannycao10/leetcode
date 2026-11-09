class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxL = 0

        l = 0
        maxFr = 0
        for r, char in enumerate(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFr = max(maxFr, count[s[r]])

            while r - l - maxFr + 1 > k:
                count[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, r - l + 1)
        
        return maxL