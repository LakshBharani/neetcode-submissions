class Solution:
    def isValid(self, s: str) -> bool:
        # d = {"[" : "]", "{" : "}", "(": ")"}
        # stack = [0]
        # for i in range(len(s)):
        #     if s[i] in d:
        #         stack.append(s[i])
        #     elif len(stack) > 1 and d[stack[-1]] == s[i]:
        #             stack.pop()
        #     else:
        #         return False
        # return stack == [0]

        d = { ")" : "(", "]" : "[", "}" : "{" }

        # ((()))
        # [())
        stack = []
        for b in s:
            if b not in d:
                stack.append(b)
            else:
                if len(stack) > 0 and stack[-1] == d[b]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
