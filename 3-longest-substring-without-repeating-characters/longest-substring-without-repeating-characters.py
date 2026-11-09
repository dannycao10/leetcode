class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0

        for r, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen