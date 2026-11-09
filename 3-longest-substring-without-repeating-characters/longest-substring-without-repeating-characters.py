class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxL = 0
        l = 0
        
        for r, letter in enumerate(s):
            while letter in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxL = max(maxL, len(charSet))
        
        return maxL