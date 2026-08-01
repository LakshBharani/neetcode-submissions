class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = 1
        prefix = [1]
        postfix = [1]
        lm = 1
        rm = 1

        for i in range(len(nums)):
            lm *= nums[i]
            prefix.append(lm)
        
        for i in range(len(nums) - 1, -1, -1):
            rm *= nums[i]
            postfix.append(rm)
        
        postfix.append(1)

        postfix = postfix[::-1]
        print(prefix, postfix)

        out = []
        for i in range(1, len(nums) + 1):
            print(prefix[i - 1] , postfix[i + 1])
            out.append(prefix[i - 1] * postfix[i + 1])


        return out