class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        words = {}

        for r in range(len(s)):

            if s[r] in words:
                l = max(words[s[r]] + 1, l)
                if l == r:
                    words = {s[r]: r}

            words[s[r]] = r
            count = max(count, r - l + 1)
        return count