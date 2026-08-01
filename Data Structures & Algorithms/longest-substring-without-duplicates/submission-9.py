class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        words = {}

        while r < len(s):
            if s[r] in words:
                l = max(words[s[r]] + 1, l)

            words[s[r]] = r
            count = max(count, r - l + 1)
            r += 1
        return count