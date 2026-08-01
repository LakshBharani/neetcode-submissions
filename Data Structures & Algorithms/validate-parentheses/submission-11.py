class Solution:
    def isValid(self, s: str) -> bool:
        d = {"[" : "]", "{" : "}", "(": ")"}
        stack = [0]
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            elif len(stack) > 1 and d[stack[-1]] == s[i]:
                    stack.pop()
            else:
                return False
        return stack == [0]